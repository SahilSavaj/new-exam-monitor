from database import db

class Exam_Main:
    def __init__(self):
        self.cur=db.cursor()
        self.session = db

    def process_request(self,num,sapid):
        total_quest=self.total_questions()
        resp=self.fetch_questions(num)
        answered=self.fetch_answers(sapid)
        print(total_quest,resp,answered)
        if type(resp) is str or type(total_quest) is str or type(answered) is str:
            # print()
            return 400, False
        else:
            if answered==total_quest:
                return 200,False
            elif answered<total_quest and answered!=0:
                resp = self.fetch_questions(answered+1)
                formatted_data = self.format_payload(resp,answered+1)
            else:
                resp=self.fetch_questions(num)
                formatted_data = self.format_payload(resp,num)
        return 200,formatted_data

    def upload_answers(self,question_no,sapid,ans):
        try:
            print(f"insert into student_ans(question_id,student_id,student_ans) values('{question_no}',{sapid},`{ans}`);")
            self.cur.execute(f"insert into student_ans(question_id,student_id,student_ans) values('{question_no}','{sapid}','{ans}');")
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

    def total_questions(self):
        try:
            self.cur.execute(f"select * from exam_question;")
            total_quest = len(self.cur.fetchall())
            return total_quest
        except Exception as e:
            print(e)
            return str(e)

    def fetch_answers(self,sapid):
        try:
            self.cur.execute(f"select * from student_ans where student_id={sapid}")
            answered_question=len(self.cur.fetchall())
            return answered_question
        except Exception as e:
            print(e)
            return str(e)      

    def format_payload(self,resp,num):
        question,optionA,optionB,optionC,optionD = resp
        resp_json = {
            'question' : question,
            'sapid': "60002190091",
            'optionA':optionA,
            'optionB':optionB,
            'optionC':optionC,
            'optionD':optionD,
            'question_no':num
        }

        return resp_json
