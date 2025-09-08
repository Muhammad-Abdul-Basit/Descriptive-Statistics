import mysql.connector
def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Muhammad786786",
        database="sakila"
    )
    return conn
