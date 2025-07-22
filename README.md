# Iris Flower Classification API

This is a simple machine learning project that predicts the species of an Iris flower based on four input features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

The project uses a Logistic Regression model trained on the famous Iris dataset. The model is deployed as an API using Flask.

## How It Works

1. The model is trained and saved using `joblib`.
2. A Flask app loads the model and exposes an endpoint at `/predict`.
3. You can send a POST request with flower measurements, and get the predicted class in response.

## Example Request

```
POST http://127.0.0.1:5000/predict
Content-Type: application/json

{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

## Example Response

```
{
  "prediction": 0
}
```

## Requirements

* Python 3.x
* Flask
* scikit-learn
* joblib

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Running the App

```bash
python app.py
```

Then test using Postman or Curl.

---

This is a great beginner-friendly project to learn about APIs and model deployment in machine learning.
