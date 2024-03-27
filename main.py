import pandas as pd
import joblib

# trained model load
model_rf = joblib.load('''NAMA MODEL YANG UDAH DI TRAIN GAES''')

def predict():
    # Get user inputs from the form
    features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
                'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']