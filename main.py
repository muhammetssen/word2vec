from gensim.models import KeyedVectors
from flask import Flask, json, request, json

app = Flask(__name__)

@app.route("/evaluate", methods=["POST"])
def evaluate():
    json_data = json.loads(request.data)
    positive_keywords = json_data["positive_keywords"]
    negative_keywords = json_data["negative_keywords"]
    result = word_vectors.most_similar(positive=positive_keywords,negative=negative_keywords)

    response = app.response_class(
        response=json.dumps({"result":result}),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    word_vectors = KeyedVectors.load_word2vec_format('trmodel', binary=True)
    from waitress import serve
    serve(app,host='0.0.0.0',port=3001)