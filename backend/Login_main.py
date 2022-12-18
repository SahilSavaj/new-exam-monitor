from database import db
import os
from helpers import decrypter
from FaceVerify_main import FaceVerify

#extra import
import cv2
import base64
import numpy as np

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
                db_image=creds_data[0][2].decode('ascii')
                print(db_image[:12])
                print(image[:20])

                #! Below code is to see image while debug
                # image = cv2.imdecode(db_image, cv2.IMREAD_COLOR)
                # encoded_data = db_image.split(',')[1]
                # nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
                # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                # encoded_data = image.split(',')[1]
                # nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
                # img2 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                # # cv2.imshow("image"  , img)
                # cv2.imshow("image", img2)
                # cv2.waitKey(0)   
                # cv2.destroyAllWindows()
                #!

                #? Face matching code here
                face_match=FaceVerify.match_face(db_image,image)
                #?
                print(face_match)
                if face_match.get('verified')==True:
                    return [True,"password matched"]
                else:
                    return [False,"face"]
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
                q='''SELECT sapid FROM users WHERE username= %s'''
                self.pointer.execute(q,(username,))
                # creds_data=self.pointer.fetchall()
                sap_data=self.pointer.fetchall()[0][0]
                print(sap_data)
                return 200,{"sapid":int(sap_data),"status":"User Found."}
            elif log_check[0]==False:
                if log_check[1]=='password':
                    return 400,'Password is not valid.'
                elif log_check[1]=='username':
                    return 400,'Username is not valid.'
                elif log_check[1]=='face':
                    return 400,'Face verification failed.'
        except Exception as err: 
            return 500,str(err)