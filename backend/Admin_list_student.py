from database import db

class Admin_List_Student:
    def __init__(self):
        self.cur=db.cursor()
        self.session = db

    def process_request(self,data):
        resp = self.get_student_details(data)
        if type(resp) == str:
            return 500,resp
        return 200,"student details fetched successfully!!"

    def get_student_details(self,data):
        try:
            print('fetching students from the database')
            self.cur.execute(f"SELECT * FROM users where is_admin = 2 AND sapid = '{data['sapid']}';")
            student_list = self.cur.fetchall()
            if not student_list:
                print('no record found in the database')
                return 'No data found from database'
        except Exception as e:
            print(e)
            return str(e)
    