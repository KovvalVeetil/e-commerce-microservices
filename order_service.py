from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []

#Create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    order = request.json
    orders.append(order)
    return jsonify(order), 201

#Retrieve order details
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = next((o for o in orders if o['id'] == order_id), None)
    return jsonify(order), 200 if order else 404

#Retrieve all orders for a specific user
@app.route('/orders/user/<int:user_id>', methods=['GET'])
def get_user_orders(user_id):
    user_orders = [o for o in orders if o['user_id'] == user_id]
    return jsonify(user_orders), 200

if __name__ == '__main__':
    app.run(port=5002)