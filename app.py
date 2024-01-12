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

    sentense = request.args.get('sentense')
    if sentense is None:
        return "Please provide ?sentense=your+sentense to lemmatize"

    doc = nlp(sentense)

    json  = doc.to_json()

    for idx,w in enumerate(doc):
        json["tokens"][idx]["token"] = w.text

    return json
