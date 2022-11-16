from database import db
import os
from helpers import encrypter
# from dotenv import load_dotenv

# load_dotenv()
ENCRYPT_DECRYPT_KEY=os.getenv('ENCRYPTION_PASS')

class Register:
    def __init__(self):
        self.session=db
        self.pointer=self.session.cursor()
        

    def register_params(self,username,password,name,email,sapid,image,is_admin):
        q='''SELECT username FROM users WHERE username= %s '''
        self.pointer.execute(q,(username,))
        user_name=self.pointer.fetchall()
        q='''SELECT sapid FROM users WHERE sapid= %s '''
        self.pointer.execute(q,(sapid,))
        sap_id=self.pointer.fetchall()

        if sap_id!=[] and sapid==sap_id[0][0]:
            return [False,'sapid']
        elif user_name!=[] and username==user_name[0][0]:
            return [False,'username']
        else:
            print(ENCRYPT_DECRYPT_KEY,"key")
            password=encrypter(password=password,key=ENCRYPT_DECRYPT_KEY)
            q='''INSERT INTO users(username,password,name,email,sapid,image,is_admin) VALUES (%s,%s,%s,%s,%s,%s,%s)'''
            self.pointer.execute(q,(username,password,name,email,sapid,image,is_admin,))
            # self.pointer.commit()
            
            return [True,'done']
    
    # def register_user(self,username,password,name,email,sapid)
    
    def register_user(self,params):
        username=params.get('username')
        password=params.get('password')
        name=params.get('name')
        email=params.get('email')
        sapid=params.get('sapid')
        image=params.get('image')
        is_admin=params.get('is_admin')
        try:
            reg_check=self.register_params(username,password,name,email,sapid,image,is_admin)
            if reg_check[0]==False:
                if reg_check[1]=='sapid':
                    return 400,"Sapid already registered."
                return 400,"Username already registered."
            elif reg_check[0]==True:
                self.session.commit()
                return 200,'Registeration Completed.'
        except Exception as err: 
            return 400,err