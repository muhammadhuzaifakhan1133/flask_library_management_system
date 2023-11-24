def search_book_query(db_conn, title, description, category_id, page):
    query = "SELECT * FROM book"
    if title is not None or description is not None or category_id is not None:
        query += " WHERE "
        if title is not None:
            query += f"title LIKES '{title}'"
            if description is not None or category_id is not None:
                query += " AND "
        if description is not None:
            query += f"description LIKES '{description}'"
            if category_id is not None:
                query += " AND "
        if category_id is not None:
            query += f"category_id={category_id}"
    if (page != None):
        query += f" LIMIT 10 OFFSET {(page-1)*10}"
    else:
        query += f" LIMIT 10 OFFSET 0"
    cur = db_conn.cursor()
    cur.execute(query)
    return cur.fetchall()
