from flask import Flask
from random import random

from flask.json import jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    result = ""
    prob = random()

    if prob > 0.5:
        result = "sim"
    else:
        result = "não"
    
    return jsonify({'resultado': result, 'probabilidade': prob})

if __name__ == "__main__":
    app.run()