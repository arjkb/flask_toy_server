from flask import Flask, request

app = Flask(__name__)

@app.route('/reverse', methods=['POST'])
def reverse():
    try:
        s = request.json['word']
    except KeyError:
        s = None

    if s is None:
        result = {
            "error" : "No body given"
        }, 400
    else:
        result = {
            "reversed" : s[::-1]
        }

    return result

@app.route('/')
def hello():
    return {
        "hello" : "world"
    }