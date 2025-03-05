import requests
import re
import os

# URL of the plain text file for Moby Dick 
BOOK_URL = "https://www.gutenberg.org/cache/epub/2701/pg2701.txt"
CORPUS_FILE = "corpus.txt"

def download_corpus(url, file_path):
    """Download the book text and save it to a file."""
    response = requests.get(url)
    response.raise_for_status()
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(response.text)
    
    print(f"Download complete: {file_path}")

def preprocess_corpus(file_path):
    """Read and clean the corpus text."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().lower()
    
    words = re.findall(r'\b[a-zA-Z0-9]+\b', text)
    return words

if __name__ == "__main__":
    download_corpus(BOOK_URL, CORPUS_FILE)
    words = preprocess_corpus(CORPUS_FILE)
    print(f"Corpus contains {len(words)} words.")