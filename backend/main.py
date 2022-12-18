from flask import Flask,request
from flask_cors import CORS
from Login_main import Login
from Register_main import Register
from flask import render_template
from database import db
import json
from Exam_main import Exam_Main
from Admin_add_question import Admin_Add_Question
from Admin_list_student import Admin_List_Student

app=Flask(__name__)
CORS(app)

@app.route('/',methods=['GET','POST'])
def home():
	response='200'
	body='Home Page'
	resp={"response":response,"body":body}
	print(resp)
	# db.close()
	return (resp)

@app.route('/register',methods=['GET','POST'])
def reg():
	if request.method=='POST':
		try:
			register=Register()
			body = request.json
			print(type(body))
			# print(type(body))
			# body=dict(body)
			# print(body)
			response,body=register.register_user(params=body)

		except Exception as e:
			response='400'
			body=str(e)
	else:
		response='200'
		body='Registeration Page'
	print("hashah",response,body)
	
	resp={"statuscode":response,"response":body}
	print(resp)
	# db.close()
	return (resp)

@app.route('/login',methods=['GET','POST'])
def log():
	if request.method=='POST':
		try:
			login=Login()
			body = request.json
			# body=dict(body)
			response,body=login.login_user(params=body)

		except Exception as e:
			response='400'
			body=str(e)
	else:
		response='200'
		body='Login Page'
	resp={"statuscode":response,"response":body}
	print(resp)
	# db.close()
	return (resp)

@app.route('/admin',methods=['GET','POST'])
def admin():
	if request.method=='GET':
		pass
		

@app.route('/capture',methods=['GET','POST'])
def capture():
	if request.method=='POST':
		response='200'
		print(request)
		body = request.body
		print(request.body)
		body=dict(body)
		# logging.debug(body)
		# body=body
	else:
		response='400'
		body='Invalid Request'
	resp={"statuscode":response,"response":body}
	# db.close()
	return (resp)


#############################################################################################################################


'''
API workflow:
1) Displaying exam questions and options from table name "exam_questions" on frontend. 
2) Storing student ans in "student_ans" table
3) submit button will be disabled until option not selected
'''

@app.route('/exam', methods = ["POST","GET"])
def exam():
	num = 1
	client = Exam_Main()
	if request.method=='GET':
		response,resp_body = client.process_request(num)
	elif request.method=='POST':
		body=request.json
		print(body)
		num=body.get('question_no',1)
		sapid=body.get('sapid',None)
		answer=body.get('ans',None)
		if (sapid==None or sapid==''):
			resp={"statuscode":500,"response":"Invalid Request"}
			return resp
		is_ans_uploaded=client.upload_answers(num, sapid, num)
		if is_ans_uploaded:
			response,resp_body=client.process_request(num)
			if resp_body==False:
				response,resp_body=(200,"No more Questions.")
		else:
			response,resp_body=(500,"Answer not uploaded.")

	resp={"statuscode":response,"response":resp_body}
	return resp




@app.route('/admin/add_question', methods = ["GET","POST"])
def add_question():
	if request.method == 'POST':
		data = json.loads(request.data) 
		client = Admin_Add_Question()
		response,resp_body = client.process_request(data)
		resp={"statuscode":response,"response":resp_body}
		return resp


	resp={"statuscode":200,"response":"add your questions here!"}
	return resp	



@app.route('/admin/list_students', methods = ["GET","POST"])
def list_student():

	if request.methodf request.method == 'GET':	
		num = 1
		client = Exam_Main()
		response,resp_body = client.process_request(num)
		resp={"statuscode":response,"response":resp_body}
		return resp
	
	if request.method == 'POST':
		pass
 == 'POST':	
		data = json.loads(request.data) 
		client = Admin_List_Student()
		response,resp_body = client.process_request(data)
		resp={"statuscode":response,"response":resp_body}
		return resp
	resp = {"statuscode":200,"response":"search for student !!!"}
	return resp	
 
			

if __name__=='__main__':
	app.run(debug=True,host='0.0.0.0') 



#############################################################################################################################



