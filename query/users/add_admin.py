def add_admin_query(db_con, email, password):
    query = """
            INSERT INTO user (email, password, user_type) 
            VALUES (%(email)s, %(password)s, "ADMIN")
        """
    cur = db_con.cursor()
    cur.execute(
        query,
        {
            "email": email,
            "password": password,
        }
    )
    db_con.commit()
    return cur.lastrowid
