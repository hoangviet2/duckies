# Constructor for questgen
from __future__ import absolute_import

import os
from flask import Flask
def create():
    app = Flask(__name__)
    return app
