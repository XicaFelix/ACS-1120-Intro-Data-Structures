import random

def random_words(sentence_len):
  file_path = '/usr/share/dict/words'
  sampled_words = []
  sentence = ''
  total_words_seen = 0
  

  with open(file_path, 'r') as file:
    for word in file:
      total_words_seen += 1
      if len(sampled_words) < sentence_len:
        sampled_words.append(word)
      else:
        rand_int = random.randint(0, total_words_seen -1)
        if rand_int < sentence_len:
          sampled_words[rand_int] = word
  return ' '.join(sampled_words)

print(random_words(5))