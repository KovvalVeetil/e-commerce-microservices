from flask import Flask, request, jsonify

app = Flask(__name__)

payments = []

#Process a payment
@app.route('/payments', methods=['POST'])
def process_payment():
    payment = request.json
    payments.append(payment)
    return jsonify(payment), 201

#Retrieve payment details
@app.route('/payments/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    payment = next((p for p in payments if p['id'] == payment_id), None)
    return jsonify(payment), 200 if payment else 404

#Process a refund
@app.route('/payments/refund', methods=['POST'])
def process_refund():
    data = request.json
    payment_id = data.get('payment_id')
    amount = data.get('amount')
    
    payment = next((p for p in payments if p['id'] == payment_id), None)
    if payment:
        if amount > payment['amount']:
            return jsonify({'message': 'Refund amount exceeds original payment amount'}), 400
        
        # call the payment gateway API to process the refund
        success = simulate_refund_with_gateway(payment_id, amount)
        
        if success:
            payment['status'] = 'refunded'
            payment['refund_amount'] = amount
            return jsonify({'message': f'Refund processed for payment ID {payment_id}'}), 200
        else:
            return jsonify({'message': 'Failed to process refund'}), 500

    return jsonify({'message': 'Payment not found'}), 404

def simulate_refund_with_gateway(payment_id, amount):
    print(f"Processing refund for payment ID {payment_id} with amount {amount}")
    return True

if __name__ == '__main__':
    app.run(port=5000)
