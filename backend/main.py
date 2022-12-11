from flask import Flask,request
from flask_cors import CORS
from Login_main import Login
from Register_main import Register
from flask import render_template
from database import db

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
	cur=db.cursor()
	cur.execute(f"select questions,optionA,optionB,optionC,optionD from exams_questions where question_no = 1;")
	question,optionA,optionB,optionC,optionD = list(cur)[0]
	

	if request.method == "POST":
		student_ans = request.form.getlist('option')[0]
		print(student_ans)
		cur.execute(f"INSERT INTO student_ans (student_ans) VALUES ('{student_ans}');")
		db.commit()
		num = int(request.form['question_number']) + 1
		cur.execute(f"select questions,optionA,optionB,optionC,optionD from exams_questions where question_no = {num};")
		question,optionA,optionB,optionC,optionD = list(cur)[0]
		return render_template("exam.html",question=question,optionA=optionA,optionB=optionB,optionC=optionC,optionD=optionD,num=num)
	return render_template("exam.html",question=question,optionA=optionA,optionB=optionB,optionC=optionC,optionD=optionD,num=1)



if __name__=='__main__':
	app.run(debug=True,host='0.0.0.0') 



#############################################################################################################################