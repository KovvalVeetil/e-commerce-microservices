from flask import Flask, request, jsonify

app = Flask(__name__)

#In-memory product data store
products = []

#create a new product
@app.route('/products', methods=['POST'])
def create_product():
    product = request.json
    products.append(product)
    return jsonify(product), 201

#endpoint to list products
@app.route('/products', methods=['GET'])
def list_products():
    return jsonify(products), 200

#get product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return jsonify(product), 200 if product else 404

#update product by ID
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        data = request.json
        product.update(data)
        return jsonify(product), 200
    return jsonify({'message': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(port=5000)