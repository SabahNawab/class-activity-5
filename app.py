from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle  # Assuming you have saved your model as a pickle file
import sys

from main import LR  # Ensure this is the correct path
sys.modules['__main__'].LR = LR 

# Load the pre-trained model
with open('pricemodel.pkl', 'rb') as f:
    model = pickle.load(f)
    

app = Flask(__name__)

# Load your model (ensure you have the model saved as 'model.pkl')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract form data
    data = {
        'area': float(request.form['area']),
        'bedrooms': float(request.form['bedrooms']),
        'bathrooms': float(request.form['bathrooms']),
        'stories': float(request.form['stories']),
        'mainroad': int(request.form['mainroad']),
        'guestroom': int(request.form['guestroom']),
        'basement': int(request.form['basement']),
        'hotwaterheating': int(request.form['hotwaterheating']),
        'airconditioning': int(request.form['airconditioning']),
        'parking': float(request.form['parking']),
        'prefarea': int(request.form['prefarea']),
        'furnishingstatus_furnished': 1 if request.form['furnishingstatus'] == 'furnished' else 0,
        'furnishingstatus_semi-furnished': 1 if request.form['furnishingstatus'] == 'semi-furnished' else 0
    }
    
    # Convert to numpy array and make prediction
    # Adjust feature order to match the order used during training
    features = np.array([[ 
        data['area'],
        data['bedrooms'],
        data['bathrooms'],
        data['stories'],
        data['mainroad'],
        data['guestroom'],
        data['basement'],
        data['hotwaterheating'],
        data['airconditioning'],
        data['parking'],
        data['prefarea'],
        data['furnishingstatus_furnished'],
        data['furnishingstatus_semi-furnished']
    ]])
    
    prediction = model.predict(features)
    
    # Return the prediction as JSON
    return jsonify({'prediction': f'{prediction[0][0]:.2f}'})

if __name__ == '__main__':
    app.run(host="0.0.0.0")
