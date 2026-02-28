from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # allows requests from your browser

@app.route("/receive", methods=["POST"])
def receive():
    data = request.json

    print("Received sample:")
    print(data)

    # Save to file
    with open("dataset.json", "a") as f:
        f.write(json.dumps(data) + "\n")

    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)