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
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
qg = main.QGen()
@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"

@app.route("/predict", methods=["POST"])
def predict():

    if qg:
        try:
            print(type(request))
            print(request.json)
            jsondata = request.json
            if len(jsondata["input_text"]) == 0:
                return jsonify({'error': "Find 0 character in the input"})
            print(type(jsondata))
            prediction = qg.predict_mcq(jsondata)
            package = json.dumps(prediction)
            return package
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print('Train the model first')
        return jsonify({'error': "find a model"})


if __name__ == '__main__':
    port = 12345
    print('Model columns loaded')
    app.run(port=port,debug=True)

