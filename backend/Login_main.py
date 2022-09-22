from database import db
import os
from helpers import encrypter,decrypter
from dotenv import load_dotenv

load_dotenv()
ENCRYPT_DECRYPT_KEY=os.getenv('ENCRYPTION_PASS')

class Login:
    def __init__(self):
        self.pointer=db.cursor()

    def check_login_params(self,username,password):
        q='''SELECT username,password FROM users WHERE username= %s AND password= %s'''
        self.pointer.execute(q,(username,password,))
        data=self.pointer.fetchall()
        if data!=[] and (username,password)==data[0]:
            return True
        else:
            return False
    def LogUser(self,params):
        username=params.get('username')
        password=params.get('password')
        try:
            if self.check_login_params(username,password):
                return 200,"User found now verify Face"
            else:
                return 400,'username or password is not valid.'
        except Exception as err: 
            return 400,err
        finally:
            pass
        return params,200