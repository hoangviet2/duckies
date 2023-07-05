from flask import Flask, request, jsonify
import traceback
import pandas as pd
import numpy as np
import time
import nltk
nltk.download('stopwords')
from pprint import pprint
from Questgen import main
import os
import json
app = Flask(__name__)

qg = main.QGen()

@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"

@app.route("/predict", methods=["POST"])
def predict():
    if qg:
        try:
            jsondata = request.json
            print(type(jsondata))
            prediction = qg.predict_mcq(jsondata)
            package = json.dumps(prediction)
            return package

        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print('Train the model first')
        return('No model here to use')


if __name__ == '__main__':
    port = 12345
    print('Model columns loaded')
    app.run(port=port,debug=True)

