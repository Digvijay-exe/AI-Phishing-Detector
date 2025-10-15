from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

print("--- Flask app is starting ---")

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enables Cross-Origin Resource Sharing

# Load the pre-trained model and vectorizer
try:
    model = joblib.load('phishing_model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    print("Model and vectorizer loaded successfully.")
except FileNotFoundError:
    print("Error: Model or vectorizer files not found. Please run train_model.py first.")
    exit()

# This block MUST NOT be indented
@app.route('/predict', methods=['POST'])
def predict():
    """
    This function handles the prediction requests from the frontend.
    """
    data = request.get_json()
    if not data or 'text' not in data:
        # Return an error if data is not in the correct format.
        return jsonify({'error': 'Invalid data input. Missing "text" field.'}), 400
    
    email_text = data['text']
    email_vectorized = vectorizer.transform([email_text])
    prediction = model.predict(email_vectorized)

    # Use the original "Safe Email" for consistency
    result = 'Phishing Email' if prediction.item() == 1 else 'Safe Email'
    return jsonify({'prediction': result})

# This block MUST also NOT be indented
if __name__ == '__main__':
    app.run(port=5000, debug=True)

