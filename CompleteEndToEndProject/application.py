import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import Flask, request, jsonify, render_template

application = Flask(__name__)
app = application

## import ridge regressor and standard scaler
ridge_model = pickle.load(open('Models/ridge.pkl', 'rb'))
std_scaler_model = pickle.load(open('Models/scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['POST', 'GET'])
def predict_datapoint():
    if request.method == 'POST':
        pass
        data = request.form
        RH = float(data.get('RH'))
        Ws = float(data.get('Ws'))
        Rain = float(data.get('Rain'))
        FFMC = float(data.get('FFMC'))
        DMC = float(data.get('DMC'))
        ISI = float(data.get('ISI'))
        Classes = float(data.get('Classes'))
        Region = float(data.get('Region'))
        Temperature = float(data.get('Temperature'))

        input_params = std_scaler_model.transform([[RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region, Temperature]])
        prediction = ridge_model.predict(input_params)

        return render_template('home.html', result='The predicted Burn index is {}'.format(prediction[0]))

    else:
        return render_template('home.html')

if __name__ == '__main__':
    application.run(host="0.0.0.0",debug=True)