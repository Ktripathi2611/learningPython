"""
Task 3 – Load Balancer Simulation: Mock Backend Server 1
=========================================================
A simple Flask app that responds with "Hello from Server 1!"
Runs on port 5001.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Hello from Server 1!"


if __name__ == "__main__":
    print("  Mock Server 1 — running on port 5001")
    app.run(port=5001)
