import flask
import os

app = flask.Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
