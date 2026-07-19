from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"service": "Student Service Running"})

@app.route("/api/students")
def students():
    return jsonify([
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Alice"}
    ])

if __name__ == "__main__":
    app.run(port=5002, debug=True)