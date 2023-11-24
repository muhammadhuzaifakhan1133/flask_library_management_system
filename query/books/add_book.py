def add_book_query(db_conn, title, description, category_id):
    query = """
        INSERT INTO book (title, description, category_id)
        VALUES (%(title)s, %(description)s, %(category_id)s)
    """
    cur = db_conn.cursor()
    cur.execute(
        query,
        {
            "title": title,
            "description": description,
            "category_id": category_id,
        }
    )
    db_conn.commit()
    return cur.lastrowid