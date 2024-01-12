FROM python:3.12

RUN pip install -U pip setuptools wheel
RUN pip install -U spacy

RUN python -m spacy download fr_core_news_lg

RUN pip install -U Flask
RUN #pip install -U gunicorn

COPY ../app.py /app/app.py

WORKDIR /app

EXPOSE 80

#CMD ["gunicorn", "-w 1", "-b", "0.0.0.0:80", "main:app"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]
