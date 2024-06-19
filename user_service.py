from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user data store
users = []

@app.route('/users', methods=['POST'])
def create_user():
    user = request.json
    users.append(user)
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    return jsonify(user), 200 if user else 404

@app.route('/users/login', methods=['POST'])
def login():
    data = request.json
    user = next((u for u in users if u['username'] == data['username'] and u['password'] == data['password']), None)
    return jsonify({'message': 'Login successful'}) if user else jsonify({'message': 'Invalid credentials'}), 200 if user else 401

if __name__ == '__main__':
    app.run(port=5000)
