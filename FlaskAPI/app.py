import flask
from flask import Flask, jsonify, request
import json
from data_input import data_in
import numpy as np
import pickle

app = Flask(__name__)

def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model


@app.route('/predict', methods=['GET'])

def predict():
    x = np.array(data_in).reshape(1,-1)
    # load model
    model = load_models()
    prediction = model.predict(x)[0]
    response = json.dumps({'result': prediction})
    return response, 200

if __name__ == '__main__':
 application.run(debug=True)