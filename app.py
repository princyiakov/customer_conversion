from flask import Flask, request, render_template

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = CustomData(
        education=request.form.get('education'),
        investment_account=int(request.form.get('investment_account')),
        income=request.form.get('income'),
        family_size=request.form.get('family_size'),
        creditc_avg_spent=float(request.form.get('creditc_avg_spent')),
        mortgage=float(request.form.get('mortgage'))

    )

    pred_df = data.get_data_as_data_frame()
    print(pred_df)
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)
    return render_template('home.html', prediction_text=f'FINAL PREDICTION: {results}')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
