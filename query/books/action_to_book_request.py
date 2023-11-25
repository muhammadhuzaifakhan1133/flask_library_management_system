def actionToBookRequest(db_conn, borrow_id, status, admin_id):
    query = """
            UPDATE book_borrow
            SET borrow_status=%(status)s, checked_by=%(admin_id)s, checked_time=NOW()
            WHERE id=%(borrow_id)s
        """
    cur = db_conn.cursor()
    cur.execute(
        query,
        {
            "status": status,
            "admin_id": admin_id,
            "borrow_id": borrow_id
        }
    )
    db_conn.commit()
    return cur.lastrowid