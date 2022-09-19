import psycopg2

def connect_database():
    return psycopg2.connect(
    database='dbbp6ebo0ffo4d',
    user='lwwkvpsrjarzfe',
    host='ec2-52-207-90-231.compute-1.amazonaws.com',
    port=5432,
    password='57da08bf792a60fdf834f5e43958b0b0b70027564c035aa43f480f2e12d20ffb'
    )
db=connect_database()