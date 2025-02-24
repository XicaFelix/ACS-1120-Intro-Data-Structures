import re
import os
import random
from dictogram import Dictogram

class MarkovModel:
    """A Markov Model using Dictogram to store state transitions."""

    def __init__(self, n_gram=2):
        """Initialize the Markov Model with an n-gram order."""
        self.n_gram = n_gram
        self.chain = {}

    def is_valid_file_path(self, string):
      pattern = r'^[\w\-.\\/:]+$'
      return bool(re.fullmatch(pattern, string)) and os.path.isfile(string)

    def read_file(self, file_path):
      if self.is_valid_file_path(file_path):
          with open(file_path, 'r') as file:
            text = file.read().lower()
          words = re.findall(r'\b\w+\b', text)  
          return words 

    def build_model(self, file_path):
        """Build a Markov chain from a list of words."""
        words = self.read_file(file_path)
        for i in range(len(words) - self.n_gram):
            prefix = tuple(words[i:i+self.n_gram])  
            next_word = words[i+self.n_gram]

            if prefix not in self.chain:
                self.chain[prefix] = Dictogram()

            self.chain[prefix].add_count(next_word)

    def generate_sentence(self, length=10, start_with=None):
        """Generate a sentence using the Markov model."""
        if not self.chain:
            raise ValueError("Markov Model is empty. Build the model first.")

        # Choose a random starting n-gram if none provided
        if start_with is None:
            start_with = random.choice(list(self.chain.keys()))
        elif tuple(start_with.split()) not in self.chain:
            raise ValueError("Given start sequence not found in model.")
        else:
            start_with = tuple(start_with.split())

        sentence = list(start_with)
        curr_state = start_with

        for _ in range(length - self.n_gram):
            if curr_state not in self.chain:
                break

            next_word = self.chain[curr_state].sample()
            sentence.append(next_word)
            curr_state = tuple(sentence[-self.n_gram:])

        return " ".join(sentence)


if __name__ == "__main__":

    markov = MarkovModel(n_gram=2)
    markov.build_model('Code/data/sample.txt')
    
    print("Generated sentence:", markov.generate_sentence(length=6))