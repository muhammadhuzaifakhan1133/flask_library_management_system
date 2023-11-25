def mark_book_returned_query(db_conn, book_id):
    query = f"""
        UPDATE book
        SET book_status='AVAILABLE'
        WHERE id='{book_id}'
        """
    cur = db_conn.cursor()
    cur.execute(query)
    db_conn.commit()
    cur.lastrowid