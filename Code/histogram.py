import re
import os

def histogram(source):
  file_path = ''
  histogram = {}
  if is_valid_file_path(source): 
    with open(source, 'r') as file:
        for line in source:
          line = line.strip()
          histogram = merge_hist(histogram, make_hist(line))
  else:
    histogram = make_hist(source)
  return histogram
        

def make_hist(line):
  hist = {}
  words = re.findall(r'\b\w+\b', line.lower())
  for word in words:
    if word in hist:
      hist[word]+= 1
    else:
      hist[word] = 1
  return hist

def merge_hist(hist1, hist2):
  for key,value in hist2.items():
    if key in hist1:
      hist1[key] += value
  return hist1


def pretty_print_histogram(histogram, mode='count'):
  
  pretty_hist = sorted(histogram.items(), key = lambda item: item[1], reverse=True)
  print("Histogram for Text:")
  if mode == 'count':
    for word, count in pretty_hist:
      print(f"{word}: {count}")
  elif mode== 'graph':
    for word, count in pretty_hist:
      print(f"{word}: {'x'*count}")

def is_valid_file_path(string):
  pattern = r'^[\w\-.\\/:]+$'  # Matches valid file path characters
  return bool(re.match(pattern, string)) and os.path.isfile(string)

def unique_words(histogram):
  pass

text = """The pale Usher—threadbare in coat, heart, body, and brain; I see him
now. He was ever dusting his old lexicons and grammars, with a queer
handkerchief, mockingly embellished with all the gay flags of all the
known nations of the world. He loved to dust his old grammars; it
somehow mildly reminded him of his mortality.

“While you take in hand to school others, and to teach them by what
name a whale-fish is to be called in our tongue, leaving out, through
ignorance, the letter H, which almost alone maketh up the
signification of the word, you deliver that which is not true.”
—_Hackluyt._
"""
hist = histogram(text)
print(hist)
pretty_print_histogram(hist, 'graph')