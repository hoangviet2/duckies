from flask import Flask, Blueprint, request, jsonify
from clone import run
run()
# import nltk
# nltk.download('stopwords')
from model import getModel
import traceback
import json
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
qg = getModel()

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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
