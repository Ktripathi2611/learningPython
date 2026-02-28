"""
Task 2: Rate Limiter Mini
===========================
A Flask API with a sliding-window rate limiter that restricts each user
(identified by IP address) to 5 requests per 60-second window.

Endpoint:
  GET /data  – Returns sample data if rate limit is not exceeded;
               otherwise returns 429 "Too Many Requests: Try again later."

Rate-limit tracking is stored in an in-memory dictionary:
  { "client_ip": [timestamp1, timestamp2, ...], ... }
"""

import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Rate Limiter Configuration
# ---------------------------------------------------------------------------
RATE_LIMIT = 5          # Maximum requests allowed
TIME_WINDOW = 60        # Window size in seconds

# In-memory dictionary to track request timestamps per user (IP)
request_log: dict[str, list[float]] = {}


# ---------------------------------------------------------------------------
# Rate Limiter Logic
# ---------------------------------------------------------------------------
def is_rate_limited(user_id: str) -> bool:
    """
    Check whether *user_id* has exceeded the rate limit.
    - Remove timestamps older than TIME_WINDOW seconds.
    - If remaining count >= RATE_LIMIT, the user is rate-limited.
    """
    current_time = time.time()

    if user_id not in request_log:
        request_log[user_id] = []

    # Prune timestamps outside the sliding window
    request_log[user_id] = [
        ts for ts in request_log[user_id]
        if current_time - ts < TIME_WINDOW
    ]

    if len(request_log[user_id]) >= RATE_LIMIT:
        return True  # Rate limit exceeded

    # Record the current request
    request_log[user_id].append(current_time)
    return False


# ---------------------------------------------------------------------------
# API Endpoint
# ---------------------------------------------------------------------------
@app.route("/data", methods=["GET"])
def get_data():
    """
    GET /data
    Returns sample JSON data if the client is within the rate limit.
    Returns 429 if the client has exceeded 5 requests in 60 seconds.
    """
    user_id = request.remote_addr  # Use client IP as user identifier

    if is_rate_limited(user_id):
        return jsonify({
            "error": "Too Many Requests: Try again later."
        }), 429

    remaining = RATE_LIMIT - len(request_log.get(user_id, []))
    return jsonify({
        "message": "Here is your data!",
        "data": {
            "id": 1,
            "name": "Sample Item",
            "description": "This is a sample response from the rate-limited API."
        },
        "rate_limit": {
            "limit": RATE_LIMIT,
            "remaining": remaining,
            "window_seconds": TIME_WINDOW
        }
    }), 200


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 50)
    print("  Rate Limiter Mini — running on port 5001")
    print(f"  Limit: {RATE_LIMIT} requests per {TIME_WINDOW}s")
    print("=" * 50)
    app.run(debug=True, port=5001)
