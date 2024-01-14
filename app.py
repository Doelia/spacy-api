import spacy
import fr_core_news_lg
from flask import Flask, request

print("loading model...")
nlp = spacy.load("fr_core_news_lg")
nlp = fr_core_news_lg.load()
print("model loaded.")

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Spacy API!"

@app.route("/lemmatize")
def lemmatize():

    sentence = request.args.get('sentence')
    if sentence is None:
        return "Please provide ?sentence=your+sentence to lemmatize"

    doc = nlp(sentence)

    json  = doc.to_json()

    for idx,w in enumerate(doc):
        json["tokens"][idx]["token"] = w.text

    return json
