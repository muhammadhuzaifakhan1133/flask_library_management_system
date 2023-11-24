from query.users import add_admin as AddAdmin

def add_admin_controller(db, email, password):
    conn = db.connect()
    user_id = AddAdmin.add_admin_query(conn, email, password)
    db.disconnect(conn)
    return user_id