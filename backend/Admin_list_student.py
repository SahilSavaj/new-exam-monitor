from database import db
import json

class Admin_List_Student:
    def __init__(self):
        self.cur=db.cursor()
        self.session = db

    def process_request(self,data):
        resp = self.get_student_details(data)[0]
        # print(resp[0])
        payload={
            "name":resp[0],
            "username":resp[1],
            "sapid":resp[3],
            "image":str(resp[2])
        }
        
        if type(resp) == str:
            return 500,resp
        return 200,{"status":"student details fetched successfully!!","data":payload}

    def get_student_details(self,data):
        try:
            print('fetching students from the database')
            self.cur.execute(f"SELECT name,username,image,sapid FROM users where is_admin = 1 AND sapid = '{data['sapid']}';")
            student_list = self.cur.fetchall()
            if not student_list:
                print('no record found in the database')
                return 'No data found from database'
            else: 
                return student_list
        except Exception as e:
            print(e)
            return str(e)
    