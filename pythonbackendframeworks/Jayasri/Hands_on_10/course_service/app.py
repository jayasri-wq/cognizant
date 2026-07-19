from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"service": "Course Service Running"})

@app.route("/api/courses")
def courses():
    return jsonify([
        {"id": 1, "name": "Python"},
        {"id": 2, "name": "Flask"}
    ])

if __name__ == "__main__":
    app.run(port=5001, debug=True)