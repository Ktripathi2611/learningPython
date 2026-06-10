import sqlite3
import string
import os
from flask import Flask, request, jsonify, redirect, g

app = Flask(__name__)

# -----------------------------
# Database Configuration
# -----------------------------
DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "urls.db")


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = sqlite3.connect(DATABASE)
    db.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_id TEXT UNIQUE NOT NULL,
            original_url TEXT NOT NULL
        )
    """)
    db.commit()
    db.close()


# -----------------------------
# Base62 Encoding
# -----------------------------
BASE62_CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits


def base62_encode(num):
    if num == 0:
        return BASE62_CHARS[0]

    result = []

    while num > 0:
        num, remainder = divmod(num, 62)
        result.append(BASE62_CHARS[remainder])

    return "".join(reversed(result))


# -----------------------------
# API: Shorten URL
# -----------------------------
@app.route("/shorten", methods=["POST"])
def shorten_url():

    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "Please provide a URL"}), 400

    original_url = data["url"]

    db = get_db()

    # Check if URL already exists
    existing = db.execute(
        "SELECT short_id FROM urls WHERE original_url = ?",
        (original_url,)
    ).fetchone()

    if existing:
        short_id = existing["short_id"]

    else:
        cursor = db.execute(
            "INSERT INTO urls (short_id, original_url) VALUES (?, ?)",
            ("temp", original_url)
        )
        db.commit()

        row_id = cursor.lastrowid

        short_id = base62_encode(row_id)

        db.execute(
            "UPDATE urls SET short_id = ? WHERE id = ?",
            (short_id, row_id)
        )
        db.commit()

    short_url = request.host_url + short_id

    return jsonify({
        "short_id": short_id,
        "short_url": short_url
    }), 201


# -----------------------------
# API: Redirect Short URL
# -----------------------------
@app.route("/<short_id>", methods=["GET"])
def redirect_url(short_id):

    db = get_db()

    row = db.execute(
        "SELECT original_url FROM urls WHERE short_id = ?",
        (short_id,)
    ).fetchone()

    if row is None:
        return jsonify({"error": "Short URL not found"}), 404

    return redirect(row["original_url"], code=302)


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    init_db()

    print("=" * 40)
    print("URL Shortener Running")
    print("http://127.0.0.1:5000")
    print("=" * 40)

    app.run(debug=True, port=5000)