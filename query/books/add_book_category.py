def add_book_category(db_conn, name):
    query = "INSERT INTO book_category (name) VALUES (%(name)s)"
    cur = db_conn.cursor()
    cur.execute(query, {"name": name})
    db_conn.commit()
    return cur.lastrowid