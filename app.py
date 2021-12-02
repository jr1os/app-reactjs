from flask import flask

app = Flask()


app.route("/")
def index():
    return "hello world" 