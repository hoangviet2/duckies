# Constructor for questgen
from __future__ import absolute_import

import os
from flask import Flask
from API import app
def create():
    main = Flask(__name__)
    main.register_blueprint(app)
    return main
