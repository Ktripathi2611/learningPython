"""
Task 3 – Load Balancer Simulation: Round-Robin Load Balancer
==============================================================
A Flask-based reverse proxy that distributes incoming requests across
three backend servers in a round-robin fashion.

Backend servers:
  - Server 1: http://127.0.0.1:5001
  - Server 2: http://127.0.0.1:5002
  - Server 3: http://127.0.0.1:5003

The load balancer itself runs on port 5000.
Each incoming GET / request is forwarded to the next server in sequence.
After Server 3, it cycles back to Server 1.

Usage:
  1. Start all three backend servers first (server1.py, server2.py, server3.py).
  2. Start this load balancer script.
  3. Send requests to http://localhost:5000/ and observe round-robin behaviour.
"""

import itertools
import requests as http_requests
from flask import Flask, jsonify

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Backend server pool
# ---------------------------------------------------------------------------
BACKEND_SERVERS = [
    "http://127.0.0.1:5001",
    "http://127.0.0.1:5002",
    "http://127.0.0.1:5003",
]

# itertools.cycle creates an infinite iterator that loops through the list
server_cycle = itertools.cycle(BACKEND_SERVERS)


# ---------------------------------------------------------------------------
# Load Balancer Endpoint
# ---------------------------------------------------------------------------
@app.route("/", methods=["GET"])
def load_balance():
    """
    Forward the incoming request to the next backend server (round-robin)
    and return its response to the client.
    """
    target_server = next(server_cycle)

    try:
        response = http_requests.get(target_server, timeout=5)
        return jsonify({
            "response": response.text,
            "served_by": target_server
        }), response.status_code

    except http_requests.exceptions.ConnectionError:
        return jsonify({
            "error": f"Backend server {target_server} is unreachable."
        }), 502


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 55)
    print("  Round-Robin Load Balancer — running on port 5000")
    print("  Distributing traffic to:")
    for s in BACKEND_SERVERS:
        print(f"    → {s}")
    print("=" * 55)
    app.run(debug=True, port=5000)
