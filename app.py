from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, this is code is updated locally Web App running on Flask Framework!"

