from flask import Flask, request, jsonify
from flask_cors import CORS
from handStructure import build_hand_from_flat
import json

app = Flask(__name__)
CORS(app)  # allows requests from your browser

@app.route("/receive", methods=["POST"])
def receive():
    data = request.json

    features = data["features"]
    label = data["label"]

    hand = build_hand_from_flat(features)

    print("Index Tip Y: ", hand.index.tip.y)

    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(port=5000, debug=True)