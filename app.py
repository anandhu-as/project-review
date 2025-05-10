from flask import Flask, request 
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('titanic.pkl','rb'))

@app.route('/')
def home():
    return 'Titanic Survival Prediction API'

@app.route('/predict',methods=['POST'])
def predict():
    data = request.get_json(force=True)

    features = [
        data['Pclass'],
        data['Sex'],
        data['Age']
    ]

    prediction = model.predict(([np.array(features)]))

    return f"Survival Prediction: {int(prediction[0])}"

if __name__ == '__main__':
    app.run(debug=True)
