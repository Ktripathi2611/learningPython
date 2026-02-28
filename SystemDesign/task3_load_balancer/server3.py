"""
Task 3 – Load Balancer Simulation: Mock Backend Server 3
=========================================================
A simple Flask app that responds with "Hello from Server 3!"
Runs on port 5003.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Hello from Server 3!"


if __name__ == "__main__":
    print("  Mock Server 3 — running on port 5003")
    app.run(port=5003)
