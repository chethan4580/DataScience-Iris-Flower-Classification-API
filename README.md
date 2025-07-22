🌸 Iris Flower Classification API
This is an end-to-end machine learning project that classifies iris flower species based on input features. The model is built using Logistic Regression and deployed via a Flask API, allowing real-time predictions through JSON input.
________________________________________
🔧 Tech Stack
•	Python 🐍
•	scikit-learn (for model building)
•	Flask (for API deployment)
•	Postman / Curl (for API testing)
________________________________________
📊 Features Used
Feature Name	Description
Sepal Length (cm)	Length of the outer part of the flower
Sepal Width (cm)	Width of the outer part
Petal Length (cm)	Length of the inner petals
Petal Width (cm)	Width of the inner petals
________________________________________
🎯 Model Output
The model classifies iris flowers into:
•	0 → Setosa
•	1 → Versicolor
•	2 → Virginica
________________________________________
📫 How to Use the API
🚀 Start the Server
python app.py
✅ Send a POST Request
URL:
http://127.0.0.1:5000/predict
Body (raw JSON):
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
Response:
{
  "prediction": 0
}
________________________________________
📁 Files Included
File	Description
app.py	Flask app with model training + API
model.pkl	Trained ML model
scaler.pkl	Scaler for preprocessing
requirements.txt	Python dependencies
________________________________________
📦 Installation (Local)
pip install -r requirements.txt
python app.py
________________________________________
🌐 This project is ideal for learning how to train, save, and deploy a simple ML model as an API.
