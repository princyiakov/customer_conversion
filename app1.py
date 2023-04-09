import pickle
from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

model = joblib.load(open('model/pipeline_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()

    # Convert the input data to a pandas dataframe
    X = pd.DataFrame(data, index=[0])
    # Define the data types of the columns to be changed
    to_change = {'family_size': 'int64', 'investment_account': 'int64',
                 'income': 'float64',
                 'creditc_avg_spent': 'float64',
                 'mortgage': 'float64'
                 }
    # Create a new dictionary with the changed data types
    for col, dtype in to_change.items():
        X[col] = np.array(X[col], dtype=dtype)

    output = model.predict(X)
    prediction = "Will take Personal Loan" if output[0]==1 else "Will NOT take Personal Loan"
    return render_template("home.html",prediction_text=f'FINAL PREDICTION: {prediction}')


if __name__ == "__main__":
    app.run(debug=True)
