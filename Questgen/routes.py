from flask import Flask, request, jsonify
import traceback
import json
from model import qg
@app.route('/')
def hello():
    return "Welcome to machine learning model APIs!"

@app.route('/predict', methods=["POST"])
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
