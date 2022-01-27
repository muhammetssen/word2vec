FROM docker.io/python:3.6.9-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
RUN wget -q http://nlp.cmpe.boun.edu.tr/staticFiles/word2vec/trmodel

EXPOSE 3001
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
