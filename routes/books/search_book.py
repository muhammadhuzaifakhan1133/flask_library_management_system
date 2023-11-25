from flask import Blueprint, request
from db import db
from controllers.books import search_book as SearchBook
from flask_jwt_extended import jwt_required

search_book_bp = Blueprint("search_book", "user_service")

@search_book_bp.route("/search-book", methods=["GET"])
@jwt_required()
def search_book_route():
    if not request.is_json:
        return {
            "error": {
                "message": "API accept JSON data"
            }
        }, 400
    data = request.get_json()
    books =  SearchBook.search_book_controller(
        db,
        title=data.get("title"),
        description=data.get("description"),
        category_id=data.get("category_id"),
        page=data.get("page"),
    )
    return {
        "data": {
            "books": books
        }
    }, 200
    
    