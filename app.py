from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model (make sure the model.pkl file is in the same directory as this script)
model = joblib.load('model\Recommender.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON request
    data = request.get_json(force=True)
    
    # Assuming the incoming request has the required number of features
    try:
        # Convert the input data into a list of lists as required by the model
        features = [list(data.values())]
        
        # Make prediction
        prediction = model.predict(features)
        
        # Return the prediction
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)


# curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"feature1": value1, "feature2": value2, "feature3": value3}' for local test.
