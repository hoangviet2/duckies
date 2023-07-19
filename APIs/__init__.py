import os
from flask import Flask
from Questgen import model
from flask_cors import CORS
def createApp():
    app = Flask(__name__)
    CORS(app)
    return app