from database import db

class Admin_Add_Question:
    def __init__(self):
        self.cur=db.cursor()
        self.session = db

    def process_request(self,data):
        resp = self.append_data_to_database(data)
        if type(resp) == str:
            return 500,resp
        return 200,"data submited successfully!!"

    def append_data_to_database(self,data):
        try:
            print('adding question to the database!!')
            self.cur.execute(f"INSERT INTO exam_question (questions,optionA,optionB,optionC,optionD,Answers) VALUES ('{data['questions']}','{data['optionA']}' ,'{data['optionB']}','{data['optionC']}','{data['optionD']}','{data['Answers']}');")
            self.session.commit()
            print('question added to the database successfully!!!')
        except Exception as e:
            print(e)
            return str(e)
    