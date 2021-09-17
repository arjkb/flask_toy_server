This is a simple toy server written in Flask, to use as a dummy server for other apps that I write.

#### How to run:

Ensure you are in a python3 environment with [flask installed](https://flask.palletsprojects.com/en/2.0.x/installation/).

To install flask, run
```
pip install Flask
```

To run the app in a development environment (debug mode):
```
export FLASK_APP=app
export FLASK_ENV=development
flask run
```