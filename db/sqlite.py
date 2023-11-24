import pymysql


def connect():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="root",
        db='library_management_sys',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

def disconnect(conn):
    conn.close()
    