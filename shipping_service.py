from flask import Flask, request, jsonify

app = Flask(__name__)

shipments = []

@app.route('/shipments', methods=['POST'])
def create_shipment():
    shipment = request.json
    shipments.append(shipment)
    return jsonify(shipment), 201

@app.route('/shipments/<int:shipment_id>', methods=['GET'])
def get_shipment(shipment_id):
    shipment = next((s for s in shipments if s['id'] == shipment_id), None)
    return jsonify(shipment), 200 if shipment else 404

@app.route('/shipments/<int:shipment_id>', methods=['PUT'])
def update_shipment(shipment_id):
    shipment = next((s for s in shipments if s['id'] == shipment_id), None)
    if shipment:
        data = request.json
        shipment.update(data)
        return jsonify(shipment), 200
    return jsonify({'message': 'Shipment not found'}), 404

if __name__ == '__main__':
    app.run(port=5000)
