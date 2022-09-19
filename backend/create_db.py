import psycopg2

def connect_database():
    global db
    db=psycopg2.connect(
    database='dbbp6ebo0ffo4d',
    user='lwwkvpsrjarzfe',
    host='ec2-52-207-90-231.compute-1.amazonaws.com',
    port=5432,
    password='57da08bf792a60fdf834f5e43958b0b0b70027564c035aa43f480f2e12d20ffb'
    )
connect_database()

# creating DB
# cursor.execute(''' CREATE TABLE users (
# 	name VARCHAR(255),
# 	username VARCHAR(255),
# 	password VARCHAR,
# 	email VARCHAR(255),
# 	sapid INT,
#     image VARCHAR,
# 	PRIMARY KEY (username,sapid)
# )''')

# ADDING DATA TO DB 

cursor=db.cursor()  

# cursor.execute(''' INSERT INTO users(name,username,password,email,sapid,image) VALUES(
#     'sahilsavaj',
#     'sahilsavaj',
#     'sahil121',
#     'sahilsad',
#     12342,
#     'sahi3l');''')


cursor.execute('SELECT username,password FROM users;')
# print(x)
print(cursor.fetchall())
db.commit()
db.close()