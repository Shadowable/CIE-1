from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/")
def home():
    return "Hello, Flask!"


@app.get("/api/greeting")
def get_greeting():
    name = request.args.get("name", "World")
    return jsonify(message=f"Hello, {name}!")


@app.post("/api/greeting")
def post_greeting():
    data = request.get_json(silent=True)
    name = data.get("name") if isinstance(data, dict) else None
    if not isinstance(name, str) or not name.strip():
        return jsonify(error="Send a non-empty 'name' in the JSON body."), 400

    return jsonify(message=f"Hello, {name.strip()}!")


if __name__ == "__main__":
    app.run(debug=True)