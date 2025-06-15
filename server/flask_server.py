from flask import Flask, request, jsonify

app = Flask(__name__)

# temporary user data (no DB)
users = {}
games = [
    {"id": 1, "name": "God of War"},
    {"id": 2, "name": "Uncharted 4"},
    {"id": 3, "name": "The Last of Us"}
]

# server route
@app.route('/')
def index():
    return "PSN Simulator Server is running."

# user signup endpoint
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = password
    return jsonify({"message": "Signup successful"}), 200

# user signin endpoint
@app.route("/signin", methods=["POST"])
def signin():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if users.get(username) != password:
        return jsonify({"error": "Invalid credentials"}), 401
    return jsonify({"message": "Signin successful"}), 200

# get user list endpoint
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"users": users}), 200

# get store list endpoint
@app.route("/store", methods=["GET"])
def store():
    return jsonify({"games": games}), 200

if __name__ == "__main__":
    app.run(debug=True)
