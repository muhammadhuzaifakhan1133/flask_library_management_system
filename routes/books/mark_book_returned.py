from flask import Blueprint, request
from db import db
from controllers.books import mark_book_returned as MarkBookReturned
from flask_jwt_extended import jwt_required, get_jwt_identity

mark_book_returned_bp = Blueprint("mark-book-return", "user_service")

@mark_book_returned_bp.route("/mark-book-return", methods=["PUT"])
@jwt_required()
def mark_book_returned_route():
    decoded_data = get_jwt_identity()
    if (decoded_data["type"] != "ADMIN"):
        return {"error": {"message": "Unauthenticated user"}}, 400
    if not request.is_json:
        return {
            "error": {
                "message": "API accept JSON data"
            }
        }, 400
    data = request.get_json()
    if (error := validate_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    bookId =  MarkBookReturned.mark_book_returned_controller(
        db, book_id=data.get("book_id")
    )
    return {
        "data": {
            "message": "Book returned successfully"
        }
    }, 200
    

def validate_data(data):
    error_msg = None
    if data.get("book_id") is None or len(str(data.get("book_id")).strip()) == 0:
        error_msg = "book_id field is required"
    return error_msg
    