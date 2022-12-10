import sys

import mariadb


try:
     con = mariadb.connect( 

    user="Ridham@localhost", 

    password="Ridham@12389", 

    host="localhost", 

    port=3306, 

    database="Exam_monitoring" 

)

except mariadb.Error as ex: 

    print(f"An error occurred while connecting to MariaDB: {ex}") 

    sys.exit(1) 


# Get Cursor 

cur = con.cursor()