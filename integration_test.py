import requests

# Base URLs for each microservice
USER_SERVICE_URL = "http://localhost:5000"
PRODUCT_SERVICE_URL = "http://localhost:5001"
ORDER_SERVICE_URL = "http://localhost:5002"
PAYMENT_SERVICE_URL = "http://localhost:5003"
SHIPPING_SERVICE_URL = "http://localhost:5004"
NOTIFICATION_SERVICE_URL = "http://localhost:5006"

# Helper function to print response
def print_response(response):
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")

# 1. Create a user
user_data = {
    "id": 1,
    "username": "testuser",
    "password": "password",
    "email": "testuser@example.com"
}
response = requests.post(f"{USER_SERVICE_URL}/users", json=user_data)
print("Create User Response:")
print_response(response)

# 2. Authenticate user
auth_data = {
    "username": "testuser",
    "password": "password"
}
response = requests.post(f"{USER_SERVICE_URL}/users/login", json=auth_data)
print("Authenticate User Response:")
print_response(response)

# 3. Add a product
product_data = {
    "id": 1,
    "name": "Test Product",
    "price": 100,
    "inventory": 10
}
response = requests.post(f"{PRODUCT_SERVICE_URL}/products", json=product_data)
print("Add Product Response:")
print_response(response)

# 4. Create an order
order_data = {
    "id": 1,
    "user_id": 1,
    "product_id": 1,
    "quantity": 1,
    "total_price": 100,
    "status": "pending"
}
response = requests.post(f"{ORDER_SERVICE_URL}/orders", json=order_data)
print("Create Order Response:")
print_response(response)

# 5. Process a payment
payment_data = {
    "id": 1,
    "user_id": 1,
    "order_id": 1,
    "amount": 100,
    "status": "paid"
}
response = requests.post(f"{PAYMENT_SERVICE_URL}/payments", json=payment_data)
print("Process Payment Response:")
print_response(response)

# 6. Create a shipment
shipment_data = {
    "id": 1,
    "order_id": 1,
    "status": "shipped",
    "tracking_number": "123456789"
}
response = requests.post(f"{SHIPPING_SERVICE_URL}/shipments", json=shipment_data)
print("Create Shipment Response:")
print_response(response)

# 7. Send a notification
notification_data = {
    "recipient": "testuser@example.com",
    "subject": "Order Shipped",
    "body": "Your order has been shipped. Tracking number: 123456789"
}
response = requests.post(f"{NOTIFICATION_SERVICE_URL}/notifications/email", json=notification_data)
print("Send Notification Response:")
print_response(response)
