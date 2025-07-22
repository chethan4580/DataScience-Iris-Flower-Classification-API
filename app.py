from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib
import numpy as np
import os

app = Flask(__name__)

# Check if model is already saved
if not os.path.exists("model.pkl") or not os.path.exists("scaler.pkl"):
    # 1. Load data
    iris = load_iris()
    X = iris.data
    y = iris.target

    # 2. Preprocess
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 3. Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # 4. Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # 5. Save model and scaler
    joblib.dump(model, "model.pkl")
    joblib.dump(scaler, "scaler.pkl")
else:
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")

@app.route('/')
def index():
    return "Welcome to the Iris Classifier API! Use POST /predict"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = np.array(data['features']).reshape(1, -1)
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
