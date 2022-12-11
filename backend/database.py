import mysql.connector

def connect_database():
    return mysql.connector.connect(
        database='online_exam',
        host='localhost',
        user='root',
        password='',
        port='3306'
    )

db=connect_database()