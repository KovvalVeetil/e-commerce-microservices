# microservices
User Service
Function: Manages user data, authentication, and authorization.
Endpoints:

POST /users: Create a new user.
GET /users/{id}: Retrieve user information.
POST /users/login: Authenticate a user.

Run and authenticate the endpoints:
pipenv shell
 export FLASK_APP=order_service.py
 export FLASK_ENV=development
 flask run --host 0.0.0.0 --port 5000

1. curl -X POST -H "Content-Type: application/json" -d '{"id": 1, "username": "testuser", "password": "testpass"}' http://localhost:5000/users

2. curl -X GET http://localhost:5000/users/1

3. curl -X POST -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpass"}' http://localhost:5000/users/login


Function: Handles product catalog, including product details, pricing, and inventory.
Endpoints:

GET /products: Retrieve a list of products.
GET /products/{id}: Retrieve details of a specific product.
POST /products: Add a new product.
PUT /products/{id}: Update product information.

Run and authenticate the endpoints:

1. curl -X GET http://localhost:5001/products

2. curl -X POST -H "Content-Type: application/json" -d '{"id": 1, "name": "Product1", "price": 100}' http://localhost:5000/products

3. curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Product1", "price": 120}' http://localhost:5000/products/1

Order Service
Function: Manages customer orders, including order creation, status updates, and history.
Endpoints:

POST /orders: Create a new order.
GET /orders/{id}: Retrieve order details.
GET /orders/user/{userId}: Retrieve all orders for a specific user.

Run and authenticate the endpoints:

1. curl -X POST -H "Content-Type: application/json" -d '{"id": 1, "user_id": 1, "total_amount": 100}' http://localhost:5000/orders

2. curl -X GET http://localhost:5002/orders/1



