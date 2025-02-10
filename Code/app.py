"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from dictogram import Dictogram

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.

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
dictogram = Dictogram(text.split())
# flask run --host=0.0.0.0 --port=5000


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    sampled_word = dictogram.sample()
    return render_template("index.html", sampled_word = sampled_word)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)