
from flask import Flask, jsonify
import os
import json

app = Flask(__name__)

# Load JSON data
data_path = "data"
data_files = [file for file in os.listdir(data_path) if file.endswith(".json")]
data_dict = {}

for file in data_files:
    file_path = os.path.join(data_path, file)
    with open(file_path, 'r') as f:
        try:
            data_dict[file.replace('.json', '')] = json.load(f)
        except json.JSONDecodeError:
            data_dict[file.replace('.json', '')] = {}

# API endpoints
@app.route('/api/<string:dataset>', methods=['GET'])
def get_dataset(dataset):
    if dataset in data_dict:
        return jsonify(data_dict[dataset])
    return jsonify({"error": "Dataset not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
