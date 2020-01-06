
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, json

import viknuapi.classifier.viknuapi as viknuapi
app = Flask(__name__)

@app.route('/')
def hello_world():
    text = str(request.args.get('text'))
    result = viknuapi.getSentenceMood(text)
    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response

