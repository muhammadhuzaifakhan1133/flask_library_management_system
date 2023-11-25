from datetime import timedelta
from flask import Flask
from routes.users import users_router_list
from routes.books import books_router_list
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
app.config["JWT_TOKEN_LOCATION"] = ["headers"] # specifying the location of JWT 
app.config["JWT_ALGORITHM"] = "HS256" # symmetric keyed hashing algorithm
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

jwt = JWTManager(app)


for route in users_router_list:
    app.register_blueprint(route)

for route in books_router_list:
    app.register_blueprint(route)


if __name__  == "__main__":
    app.run(
        debug=True,
        port=3000
    )