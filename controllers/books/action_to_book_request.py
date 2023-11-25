from query.books import action_to_book_request as ActionToBookRequest

def action_to_book_request_controller(db,borrow_id, status, admin_id):
    conn = db.connect()
    book_id = ActionToBookRequest.actionToBookRequest(conn, borrow_id, status, admin_id)
    db.disconnect(conn)
    return book_id