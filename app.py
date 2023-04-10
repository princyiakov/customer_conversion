from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

model = joblib.load(open('model/rf_model.pkl', 'rb'))
cat_fillnan = joblib.load(open('model/cat_fillnan.pkl', 'rb'))
num_fillnan = joblib.load(open('model/num_fillnan.pkl', 'rb'))
encoder = joblib.load(open('model/endoder.pkl', 'rb'))
scalar = joblib.load(open('model/scalar.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')


def preprocess(dataframe):
    dataframe = dataframe[['education', 'investment_account', 'income', 'family_size', 'creditc_avg_spent', 'mortgage']]
    cols_to_encode = ['education', 'investment_account']
    cols_to_scale = ['income', 'family_size', 'creditc_avg_spent', 'mortgage']

    dataframe = dataframe.replace('', np.nan)

    # Define the data types of the columns to be changed
    to_change = {'family_size': 'int64', 'investment_account': 'int64',
                 'income': 'float64',
                 'creditc_avg_spent': 'float64',
                 'mortgage': 'float64'
                 }
    # Create a new dictionary with the changed data types
    for col, dtype in to_change.items():
        dataframe[col] = np.array(dataframe[col], dtype=dtype)

    dataframe[cols_to_encode] = cat_fillnan.transform(dataframe[cols_to_encode])
    dataframe[cols_to_scale] = num_fillnan.transform(dataframe[cols_to_scale])
    dataframe[cols_to_encode] = encoder.transform(dataframe[cols_to_encode])
    dataframe[cols_to_scale] = scalar.transform(dataframe[cols_to_scale])

    return dataframe


@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()

    # Convert the input data to a pandas dataframe
    df = pd.DataFrame(data, index=[0])
    df = preprocess(df)

    output = model.predict(df)
    prediction = "Will take Personal Loan" if output[0] == 1 else "Will NOT take Personal Loan"
    return render_template("home.html", prediction_text=f'FINAL PREDICTION: {prediction}')


if __name__ == "__main__":
    app.run(debug=True)
