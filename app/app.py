from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "DevOps Learning Dashboard",
        "status": "running",
        "message": "Docker Compose project is working!"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/db")
def database():
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()

        cursor.close()
        connection.close()

        return jsonify({
            "database": "connected",
            "postgresql": version[0]
        })

    except Exception as error:
        return jsonify({
            "database": "connection failed",
            "error": str(error)
        }), 500
@app.route("/topics")
def topics():
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

        cursor = connection.cursor()

        cursor.execute(
            "SELECT topic, status FROM learning_topics ORDER BY id;"
        )

        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify([
            {
                "topic": topic,
                "status": status
            }
            for topic, status in rows
        ])

    except Exception as error:
        return jsonify({
            "error": str(error)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
