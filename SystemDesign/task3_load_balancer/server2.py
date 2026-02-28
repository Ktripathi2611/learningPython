"""
Task 3 – Load Balancer Simulation: Mock Backend Server 2
=========================================================
A simple Flask app that responds with "Hello from Server 2!"
Runs on port 5002.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Hello from Server 2!"


if __name__ == "__main__":
    print("  Mock Server 2 — running on port 5002")
    app.run(port=5002)
