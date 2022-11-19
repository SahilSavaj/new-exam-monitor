from flask import Flask,request
from flask_cors import CORS
from Login_main import Login
from Register_main import Register


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
            body=e
    else:
        response='200'
        body='Registeration Page'
    resp={"statuscode":response,"response":body}
    # print(resp)
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
            body=e
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


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0') 