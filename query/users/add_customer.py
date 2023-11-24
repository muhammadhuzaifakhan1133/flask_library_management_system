def add_customer_query(db_con, email, password):
    query = """
            INSERT INTO user (email, password, user_type) 
            VALUES (%(email)s, %(password)s, "CUSTOMER")
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
