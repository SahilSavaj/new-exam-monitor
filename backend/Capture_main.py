from database import db
import os
# from FaceVerify_main import FaceVerify

#extra import
import cv2 as cv
import base64
import numpy as np

folder=os.path.dirname(__file__)
class Capture:
    def __init__(self):
        # self.pointer=db.cursor()
        pass

    def Check_face_frames(self,image):
        try:    
            faces  = cv.CascadeClassifier(os.path.join(folder,'face.xml'))
            eyes = cv.CascadeClassifier(os.path.join(folder,'eye.xml'))
            encoded_data = image.split(',')[1]
            nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
            img = cv.imdecode(nparr, cv.IMREAD_COLOR)
            face = faces.detectMultiScale(img,1.1,5)
            if len(face) > 0:
                for (x,y,w,h) in face:
                    eyes_gray = img[y:y+h,x:x+w]
                    eyes_img = img[y:y+h,x:x+w]
                    eye = eyes.detectMultiScale(eyes_gray,1.4,5)
                    if len(eye) >= 1:
                        for (ex,ey,ew,eh) in eye:
                            eye = True
                            msg="Eye detected"
                    else:
                        msg="Eye not detected"
                        eye = False       
            else:
                eye = False
                msg="face not detected"       

            return 200,msg
        except Exception as e:
            print(e)
            return 500,False
