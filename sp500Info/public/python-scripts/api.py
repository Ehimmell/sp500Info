from flask import Flask, request, jsonify
import dataInteract as di
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE"], "allow_headers": "*"}})

@app.route('/api/daily-prediction', methods=['GET'])
def get_prediction():
    prediction = di.getDailyPrediction()
    print(prediction)
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True)