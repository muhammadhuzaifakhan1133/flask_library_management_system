import sys

sys.path.append(".")
from app import app
from query.books.add_book_category import add_book_category
from db import db


def test_create_book_api():
    login_response = app.test_client().post(
        "/login",
        json={"email": "huzaifa@gmail.com", "password": "123456", "user_type": "ADMIN"},
    )
    con = db.connect()
    category_id = add_book_category(con, "action")
    db.disconnect(con)
    response = app.test_client().post(
        "/add-book",
        query_string={"token": login_response.json["token"]},
        json={
            "title": "new book",
            "description": "This is description",
            "category_id": category_id,
        },
    )
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert data["data"] is not None
    assert data["data"]["id"] > 0

def test_create_book_api_without_token():
    login_response = app.test_client().post(
        "/login",
        json={"email": "huzaifa@gmail.com", "password": "123456", "user_type": "ADMIN"},
    )
    con = db.connect()
    category_id = add_book_category(con, "action")
    db.disconnect(con)
    response = app.test_client().post(
        "/add-book",
        json={
            "title": "new book",
            "description": "This is description",
            "category_id": category_id,
        },
    )
    data = response.json
    print(data)
    assert data is not None
    assert type(data) is dict
    assert data["error"] is not None
    assert data["error"]["message"] == "Unauthenticated user"

def test_create_book_api_without_title():
    login_response = app.test_client().post(
        "/login",
        json={"email": "huzaifa@gmail.com", "password": "123456", "user_type": "ADMIN"},
    )
    con = db.connect()
    category_id = add_book_category(con, "action")
    db.disconnect(con)
    response = app.test_client().post(
        "/add-book",
        query_string={"token": login_response.json["token"]},
        json={
            "description": "This is description",
            "category_id": category_id,
        },
    )
    data = response.json
    print(data)
    assert data is not None
    assert type(data) is dict
    assert data["error"] is not None
    assert data["error"]["message"] == "title field is required"

def test_create_book_api_without_description():
    login_response = app.test_client().post(
        "/login",
        json={"email": "huzaifa@gmail.com", "password": "123456", "user_type": "ADMIN"},
    )
    con = db.connect()
    category_id = add_book_category(con, "action")
    db.disconnect(con)
    response = app.test_client().post(
        "/add-book",
        query_string={"token": login_response.json["token"]},
        json={
            "title": "new book",
            "category_id": category_id,
        },
    )
    data = response.json
    print(data)
    assert data is not None
    assert type(data) is dict
    assert data["error"] is not None
    assert data["error"]["message"] == "description field is required"

def test_create_book_api_without_category_id():
    login_response = app.test_client().post(
        "/login",
        json={"email": "huzaifa@gmail.com", "password": "123456", "user_type": "ADMIN"},
    )
    response = app.test_client().post(
        "/add-book",
        query_string={"token": login_response.json["token"]},
        json={
            "title": "new book",
            "description": "This is description",
        },
    )
    data = response.json
    print(data)
    assert data is not None
    assert type(data) is dict
    assert data["error"] is not None
    assert data["error"]["message"] == "category_id field is required"

def test_borrow_book_api():
    login_response = app.test_client().post(
        "/login",
        json={"email": "hello@gmail.com", "password": "123456", "user_type": "CUSTOMER"},
    )
    response = app.test_client().post(
        "/borrow-book",
        query_string={"token": login_response.json["token"]},
        json={
            "book_id": "1",
            "from_date": "2023-11-11",
            "to_date": "2023-11-20",
        },
    )
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert data["data"] is not None
    assert data["data"]["id"] > 0

def test_action_to_book_request():
    login_response = app.test_client().post(
        "/login",
        json={"email": "huzaifa@gmail.com", "password": "123456", "user_type": "ADMIN"},
    )
    response = app.test_client().put(
        "/action-to-book-request",
        query_string={"token": login_response.json["token"]},
        json={
            "borrow_id": "1",
            "borrow_status": "ACCEPT",
        },
    )
    data = response.json
    print(data)
    assert data is not None
    assert type(data) is dict
    assert data["data"] is not None
    assert data["data"]["message"] == "borrow request updated successfully"

def test_mark_book_returned():
    login_response = app.test_client().post(
        "/login",
        json={"email": "huzaifa@gmail.com", "password": "123456", "user_type": "ADMIN"},
    )
    response = app.test_client().put(
        "/mark-book-return",
        query_string={"token": login_response.json["token"]},
        json={
            "book_id": "1",
        },
    )
    data = response.json
    print(data)
    assert data is not None
    assert type(data) is dict
    assert data["data"] is not None
    assert data["data"]["message"] == "Book returned successfully"

def test_search_book_api():
    login_response = app.test_client().post(
        "/login",
        json={"email": "hello@gmail.com", "password": "123456", "user_type": "CUSTOMER"},
    )
    response = app.test_client().get("/search-book", json={
        "title": "new"
    }, query_string = {"token": login_response.json["token"]})
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert data["data"] is not None
    assert len(data["data"]) == 1
