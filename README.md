# microservices
User Service
Function: Manages user data, authentication, and authorization.
Endpoints:

POST /users: Create a new user.
GET /users/{id}: Retrieve user information.
POST /users/login: Authenticate a user.

Run and authenticate the endpoints:
1. curl -X POST -H "Content-Type: application/json" -d '{"id": 1, "username": "testuser", "password": "testpass"}' http://localhost:5000/users

2. curl -X GET http://localhost:5000/users/1

3. curl -X POST -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpass"}' http://localhost:5000/users/login


Function: Handles product catalog, including product details, pricing, and inventory.
Endpoints:

GET /products: Retrieve a list of products.
GET /products/{id}: Retrieve details of a specific product.
POST /products: Add a new product.
PUT /products/{id}: Update product information.
