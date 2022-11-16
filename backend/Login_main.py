from database import db
import os
from helpers import decrypter
from FaceVerify_main import FaceVerify

ENCRYPT_DECRYPT_KEY=os.getenv('ENCRYPTION_PASS')

class Login:
    def __init__(self):
        self.pointer=db.cursor()

    def check_login_params(self,username,password,image):
        q='''SELECT username,password,image FROM users WHERE username= %s'''
        self.pointer.execute(q,(username,))
        creds_data=self.pointer.fetchall()
        # print(creds_data)
        if creds_data!=[]:
            db_pass=creds_data[0][1]
            decrypt_pass=decrypter(password=db_pass,key=ENCRYPT_DECRYPT_KEY)
            if password==decrypt_pass:
                db_image=creds_data[0][2]
                print(db_image,image)
                #? Face matching code here
                print(FaceVerify.match_face('/home/sahil/Downloads/1.jpg','/home/sahil/Downloads/2.jpg'))
                return [True,"password matched"]
            else:
                return [False,"password"]
        else:
            return [False,"username"]
    def login_user(self,params):
        username=params.get('username')
        password=params.get('password')
        image=params.get('image')
        try:
            log_check=self.check_login_params(username,password,image)
            if log_check[0]==True:
                return 200,"User found."
            elif log_check[0]==False:
                if log_check[1]=='password':
                    return 400,'password is not valid.'
                elif log_check[1]=='username':
                    return 400,'username is not valid.'
        except Exception as err: 
            return 400,err