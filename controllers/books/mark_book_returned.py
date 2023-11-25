from query.books import mark_book_returned as MarkBookReturned

def mark_book_returned_controller(db,book_id):
    conn = db.connect()
    book_id = MarkBookReturned.mark_book_returned_query(conn, book_id)
    db.disconnect(conn)
    return book_id