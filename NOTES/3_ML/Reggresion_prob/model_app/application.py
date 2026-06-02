import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from flask import Flask,request,jsonify,render_template
application = Flask(__name__)
app = application
###intrsct with reidge nd scaler pickle
ridge_model = pickle.load(open(r'd:\DS CODE\myspace\3_ML\model_app\regressor_R_cv.pkl','rb'))

standard_scaler = pickle.load(open(r'd:\DS CODE\myspace\3_ML\model_app\scaler.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predictdata',methods = ['GET','POST'])
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == "POST":
        print("Form data received:", request.form)  # Debugging step

        # Collect numerical input values from the form
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        # Create a list of numerical values (not column names!)
        input_data = [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]

        # Apply standard scaling
        new_scaled_data = standard_scaler.transform(input_data)

        # Make prediction
        result = ridge_model.predict(new_scaled_data)

        return render_template('home.html', result=result[0])

    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)