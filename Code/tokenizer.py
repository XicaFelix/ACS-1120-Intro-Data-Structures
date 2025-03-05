import re

def tokenize(text):
    """Tokenize text into a list of words by removing punctuation and splitting by whitespace."""
    no_punc_text = remove_punctuation(text)
    tokens = split_on_whitespace(no_punc_text)
    return tokens

def remove_punctuation(text):
    """Remove punctuation marks from the text."""
    no_punc_text = re.sub('[,.()]', '', text)
    no_punc_text = re.sub('--', ' ', no_punc_text)
    return no_punc_text

def split_on_whitespace(text):
    """Split the text by whitespace into tokens."""
    return text.split()
