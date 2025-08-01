import pickle
from flask import Flask, request, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model
model = pickle.load(open('DTreg.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = [
            float(request.form['radius_mean']),
            float(request.form['texture_mean']),
            float(request.form['perimeter_mean']),
            float(request.form['area_mean']),
            float(request.form['concavity_mean']),
            float(request.form['concave_points_mean']),
            float(request.form['symmetry_mean']),
            float(request.form['fractal_dimension_mean'])
        ]

        input_df = pd.DataFrame([input_data], columns=[
            'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
            'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean'
        ])

        prediction = model.predict(input_df)[0]
        result = 'Malignant' if prediction == 1 else 'Benign'

        return render_template('form.html', prediction_text=f"🩺 Prediction: {result}")
    
    except Exception as e:
        return f"❌ Error during prediction: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
