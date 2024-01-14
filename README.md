# spacy-api

An api on top of [spaCy](https://spacy.io/), a natural language processing library.

Model used : [fr_core_news_lg](https://spacy.io/models/fr#fr_core_news_lg)

## API Usage

### Lemmatize

Request example :
```
curl http://localhost:5000/lemmatize?sentence=j'ai%20faim
```

Response example :
```
{
   "ents": [],
   "sents": [{ "end":9, "start":0 }],
   "text": "j'ai faim",
   "tokens": [
      { "dep":"nsubj", "end":2, "head":1, "id":0, "lemma":"je", "morph":"Number=Sing|Person=1", "pos":"PRON", "start":0, "tag":"PRON", "token":"j'" },
      { "dep":"ROOT", "end":4, "head":1, "id":1, "lemma":"avoir", "morph":"Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin", "pos":"AUX", "start":2, "tag":"AUX", "token":"ai" },
      { "dep":"obj", "end":9, "head":1, "id":2, "lemma":"faim", "morph":"Gender=Fem|Number=Sing", "pos":"NOUN", "start":5, "tag":"NOUN", "token":"faim" }
   ]
}
```

## Run (with docker)

Use the pre-builded docker image from docker hub :
```
docker run -it --rm -p 5050:80 --name spacy-api doelia/spacy-api:main
```

Then navigate to http://localhost:5050/lemmatize

## Development

Dependencies :
```
pip install spacy Flask
python -m spacy download fr_core_news_lg
```

Run server :
```
flask run
```

