from query.books import search_book as SearchBook

def search_book_controller(db, title, description, category_id, page):
    conn = db.connect()
    books = SearchBook.search_book_query(conn, title, description, category_id, page)
    db.disconnect(conn)
    return books