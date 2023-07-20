import os
from flask import Flask
from Questgen import model
from flask_cors import CORS
from Questgen import clone
def createApp():

    clone.run()
    app = Flask(__name__)
    CORS(app)
    return app