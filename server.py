from flask import Flask, jsonify
from flask_cors import CORS
import random
import datetime

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/')
def get_data():
    data = {
        "sensor_id": f"sensor_{random.randint(1, 100)}",
        "borehole": f"borehole_{random.randint(1, 10)}",
        "timestamp": datetime.datetime.now().isoformat(),
        "water_level": round(random.uniform(10.0, 50.0), 2),
        "temperature": round(random.uniform(15.0, 35.0), 2),
        "pressure": round(random.uniform(1.0, 5.0), 2),
        "water_quality": round(random.uniform(1.0, 10.0), 2)
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
