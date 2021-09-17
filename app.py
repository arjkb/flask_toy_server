from logging import error
from flask import Flask, request

app = Flask(__name__)

WORD_KEY = 'word'

@app.route('/reverse', methods=['POST'])
def reverse():
    s = request.json[WORD_KEY] if WORD_KEY in request.json else None

    if s is None:
        result, error_code = {"error" : "No body given"}, 400
    else:
        result, error_code = {"reversed" : s[::-1]}, 200

    return result, error_code

@app.route('/')
def hello():
    return {
        "hello" : "world"
    }