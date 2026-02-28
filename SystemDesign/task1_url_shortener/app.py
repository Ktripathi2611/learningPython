"""
Task 1: URL Shortener Lite
===========================
A lightweight URL shortener service built with Flask and SQLite.

Endpoints:
  POST /shorten  – Accepts a long URL, returns a unique short URL ID.
  GET  /<shortId> – Redirects to the original URL.

Storage: SQLite database (urls.db)
ID Generation: Base62 encoding of the auto-increment primary key.
"""

import sqlite3
import string
import os
from flask import Flask, request, jsonify, redirect, g

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Database helpers
# ---------------------------------------------------------------------------
DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "urls.db")


def get_db():
    """Open a database connection and store it on the Flask 'g' object."""
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception):
    """Close the database connection when the request ends."""
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Create the urls table if it doesn't already exist."""
    db = sqlite3.connect(DATABASE)
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS urls (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            short_id    TEXT    UNIQUE NOT NULL,
            original_url TEXT   NOT NULL
        )
        """
    )
    db.commit()
    db.close()


# ---------------------------------------------------------------------------
# Base62 encoding
# ---------------------------------------------------------------------------
BASE62_CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits  # a-z A-Z 0-9


def base62_encode(num: int) -> str:
    """Convert a positive integer to a Base62 string."""
    if num == 0:
        return BASE62_CHARS[0]
    result = []
    while num > 0:
        num, remainder = divmod(num, 62)
        result.append(BASE62_CHARS[remainder])
    return "".join(reversed(result))


# ---------------------------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------------------------
@app.route("/shorten", methods=["POST"])
def shorten_url():
    """
    POST /shorten
    Body (JSON): { "url": "https://example.com/very/long/path" }
    Response:     { "short_url": "http://localhost:5000/b", "short_id": "b" }
    """
    data = request.get_json(force=True)
    original_url = data.get("url")

    if not original_url:
        return jsonify({"error": "Missing 'url' field in request body"}), 400

    db = get_db()

    # Check if this URL has already been shortened
    existing = db.execute(
        "SELECT short_id FROM urls WHERE original_url = ?", (original_url,)
    ).fetchone()

    if existing:
        short_id = existing["short_id"]
    else:
        # Insert the URL and use the auto-increment id for Base62 encoding
        cursor = db.execute(
            "INSERT INTO urls (short_id, original_url) VALUES (?, ?)",
            ("temp", original_url),
        )
        db.commit()
        row_id = cursor.lastrowid
        short_id = base62_encode(row_id)

        # Update with the actual short_id
        db.execute("UPDATE urls SET short_id = ? WHERE id = ?", (short_id, row_id))
        db.commit()

    short_url = f"{request.host_url}{short_id}"
    return jsonify({"short_url": short_url, "short_id": short_id}), 201


@app.route("/<short_id>", methods=["GET"])
def redirect_url(short_id):
    """
    GET /<shortId>
    Redirects (302) to the original URL that was shortened.
    """
    db = get_db()
    row = db.execute(
        "SELECT original_url FROM urls WHERE short_id = ?", (short_id,)
    ).fetchone()

    if row is None:
        return jsonify({"error": "Short URL not found"}), 404

    return redirect(row["original_url"], code=302)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    init_db()
    print("=" * 50)
    print("  URL Shortener Lite — running on port 5000")
    print("=" * 50)
    app.run(debug=True, port=5000)
