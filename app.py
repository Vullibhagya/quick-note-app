from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/notes", methods=["GET"])
def get_notes():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes ORDER BY id DESC")

    notes = []

    for row in cursor.fetchall():
        notes.append({
            "id": row[0],
            "content": row[1]
        })

    conn.close()

    return jsonify(notes)

@app.route("/notes", methods=["POST"])
def add_note():

    data = request.json

    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO notes(content) VALUES(?)",
        (data["content"],)
    )

    conn.commit()
    conn.close()

    return jsonify({"message":"Saved Successfully"})

if __name__ == "__main__":
    app.run(debug=True)