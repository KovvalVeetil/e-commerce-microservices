# Microservices

This project is a microservices-based architecture for an e-commerce application. Each microservice is responsible for a specific business function and is implemented using Python and Flask. The services are managed using pm2, which helps in running and monitoring multiple services concurrently.

## Project Overview

This project consists of several microservices for an e-commerce platform:

- User Service: Manages user data, authentication, and authorization.
- Product Service: Handles the product catalog, including details, pricing, and inventory.
- Order Service: Manages customer orders, including creation, status updates, and history.
- Payment Service: Processes payments, transactions, and manages payment methods.
- Shipping Service: Manages shipping and delivery, including shipment tracking and logistics.
- Notification Service: Sends notifications to users via email, SMS, or push notifications.

## User Service
Function: Manages user data, authentication, and authorization.
Endpoints:

POST /users: Create a new user.
GET /users/{id}: Retrieve user information.
POST /users/login: Authenticate a user.

> [!NOTE]
> Run and authenticate individual API's and services using curl/Postman:
pipenv shell
export FLASK_APP=order_service.py
export FLASK_ENV=development
flask run --host 0.0.0.0 --port 5000

1. curl -X POST -H "Content-Type: application/json" -d '{"id": 1, "username": "testuser", "password": "testpass"}' http://localhost:5000/users

2. curl -X GET http://localhost:5000/users/1

3. curl -X POST -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpass"}' http://localhost:5000/users/login

## Product Service
Function: Handles product catalog, including product details, pricing, and inventory.
Endpoints:

GET /products: Retrieve a list of products.
GET /products/{id}: Retrieve details of a specific product.
POST /products: Add a new product.
PUT /products/{id}: Update product information.

Run and authenticate the endpoints:

1. curl -X GET http://localhost:5000/products

2. curl -X POST -H "Content-Type: application/json" -d '{"id": 1, "name": "Product1", "price": 100}' http://localhost:5000/products

3. curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Product1", "price": 120}' http://localhost:5000/products/1

## Order Service
Function: Manages customer orders, including order creation, status updates, and history.
Endpoints:

POST /orders: Create a new order.
GET /orders/{id}: Retrieve order details.
GET /orders/user/{userId}: Retrieve all orders for a specific user.

Run and authenticate the endpoints:

1. curl -X POST -H "Content-Type: application/json" -d '{"id": 1, "user_id": 1, "total_amount": 100}' http://localhost:5000/orders

2. curl -X GET http://localhost:5000/orders/1

## Payment Service

Function: Processes payments, handles transactions, and manages payment methods.
Endpoints:

POST /payments: Process a payment.
GET /payments/{id}: Retrieve payment details.
POST /payments/refund: Process a refund.

Run and authenticate the endpoints:
1. curl -X POST -H "Content-Type: application/json" -d '{"id": 1, "user_id": 1, "amount": 100, "status": "paid"}' http://localhost:5003/payments

2. curl -X GET http://localhost:5003/payments/1

3. curl -X POST -H "Content-Type: application/json" -d '{"payment_id": 1, "amount": 50}' http://localhost:5003/payments/refund

## Shipping Service


## Notification service:
1. curl -X POST -H "Content-Type: application/json" -d '{"recipient": "recipient@example.com", "subject": "Test Email", "body": "This is a test email."}' http://localhost:5006/notifications/email


## Integration Testing:

### Steps to Test the Microservices:

Run Each Microservice: Ensure that each microservice (User, Product, Order, Payment, Shipping, Notification) is running on its designated port.

Integration Test Scripts: Write scripts that simulate the complete workflow, making HTTP requests to each service and verifying the responses. You can use tools like curl, Postman, or a Python script with the requests library


Docker Compose: Use Docker Compose to run all microservices in isolated containers and handle networking between them.



Testing using Postman:

1. Create a new request collection
2. Install and use pm2 to manage all microservices
npx pm2 start ecosystem.config.js
pm2 list

3. Run the entire collection

- Using pm2

```bash

cd workspace/microservice/microservice
Create the ecosystem.config.js File

Make sure this file is in the root directory of your project (workspace/microservice/microservice). Here’s an example configuration:

javascript
Copy code
module.exports = {
  apps: [
    {
      name: 'user-service',
      script: 'user_service.py',
      interpreter: 'python'
    },
    {
      name: 'product-service',
      script: 'product_service.py',
      interpreter: 'python'
    },
    {
      name: 'order-service',
      script: 'order_service.py',
      interpreter: 'python'
    },
    {
      name: 'payment-service',
      script: 'payment_service.py',
      interpreter: 'python'
    },
    {
      name: 'shipping-service',
      script: 'shipping_service.py',
      interpreter: 'python'
    },
    {
      name: 'notification-service',
      script: 'notification_service.py',
      interpreter: 'python'
    }
  ]
};
Start All Microservices with pm2:

pm2 start ecosystem.config.js
Verify Services Are Running:

pm2 list
```

