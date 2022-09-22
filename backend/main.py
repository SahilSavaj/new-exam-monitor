from crypt import methods
from flask import Flask,request
from flask_cors import CORS
import logging
from helpers import encrypter,decrypter
from Login_main import Login


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


@app.route('/login',methods=['GET','POST'])
def log():
    if request.method=='POST':
        try:
            login=Login()
            args = request.args
            args=dict(args)
            response,body=login.LogUser(params=args)

        except Exception as e:
            response='400'
            body=e
    else:
        response='400'
        body='Invalid Request'
    resp={"response":response,"body":body}
    print(resp)
    # db.close()
    return (resp)

@app.route('/capture',methods=['GET','POST'])
def capture():
    if request.method=='POST':
        response='200'
        print(request)
        args = request.args
        print(request.args)
        args=dict(args)
        # logging.debug(args)
        body=args
    else:
        response='400'
        body='Invalid Request'
    resp={"response":response,"body":body}
    # db.close()
    return (resp)


# @app.route('/register',methods=['GET','POST'])
# def register():
#     if request.method=='POST':
#         try:
#             login=Login()
            
#             args = request.args
#             args=dict(args)
#             response,body=login.LogUser(params=args)

#         except Exception as e:
#             response='400'
#             body=e
#     else:
#         response='400'
#         body='Invalid Request'
#     resp={"response":response,"body":body}
#     print(resp)
#     # db.close()
#     return (resp)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0') 