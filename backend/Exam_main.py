from database import db

class Exam_Main:
    def __init__(self):
        self.cur=db.cursor()
        self.session = db

    def process_request(self,num):
        resp = self.fetch_questions(num)

        if type(resp) is str:
            return 400,False
        print(type(resp),'rihdamshafa')
        formatted_data = self.format_payload(resp,num)
        return 200,formatted_data

    def upload_answers(self,num,sapid,question_no):
        try:
            self.cur.execute(f"insert into student_ans(question_id,student_id,student_ans) values({question_no},{sapid},{num});")
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def fetch_questions(self,num):
        try:
            self.cur.execute(f"select questions,optionA,optionB,optionC,optionD from exam_question where question_no = {num};")
            exam_data = self.cur.fetchall()[0]
            return exam_data
        except Exception as e:
            print(e)
            return str(e)
            

    def format_payload(self,resp,num):
        question,optionA,optionB,optionC,optionD = resp
        resp_json = {
            'question' : question,
            'sapid': "no sapid for now",
            'optionA':optionA,
            'optionB':optionB,
            'optionC':optionC,
            'optionD':optionD,
            'question_no':num
        }

        return resp_json
