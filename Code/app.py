"""Main script, uses other modules to generate sentences."""
import sys
import os
from flask import Flask, render_template, jsonify
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from markov_chain import MarkovModel
from tokenizer import tokenize


app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
# Initialize the Markov Model
markov = MarkovModel(n_gram=2)

def build_markov_model_from_file(file_path):
    """Read a file, tokenize its contents, and build the Markov model."""
    with open(file_path, 'r') as file:
        text = file.read().lower()
    tokens = tokenize(text)
    markov.build_model(tokens)

# Build the Markov model from the corpus
build_markov_model_from_file("data/corpus.txt")

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    generated_sentence = markov.generate_sentence(length=10)
    return render_template("index.html", generated_sentence=generated_sentence)

@app.route("/generate_sentence")
def generate_sentence():
    """API endpoint to generate a new sentence."""
    generated_sentence = markov.generate_sentence(length=10)
    return jsonify(generated_sentence=generated_sentence)

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)