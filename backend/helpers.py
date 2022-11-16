from cryptography.fernet import Fernet

def encrypter(password,key):
    # fkey=open("file_key.txt",'rb')
    # key=fkey.read()
    # key=Fernet.generate_key()
    print(key)
    cipher=Fernet(key)
    print("Value in encrypter function - ",password)
    encrypted_pass=cipher.encrypt(bytes(password,'utf-8'))
    print("Function answer by decrypter - ",encrypted_pass)
    return encrypted_pass

def decrypter(password,key):
    # fkey=open("file_key.txt",'rb')
    # key=fkey.read()
    cipher=Fernet(key)
    print("Value in decryptor function - ",password)
    decrypted_pass=cipher.decrypt(password)
    print("Function answer by decryptor - ",decrypted_pass)
    return decrypted_pass.decode()

# def store(pic,name):
#     gray_face = cv.cvtColor(pic,cv.COLOR_BGR2GRAY)
#     face = faces.detectMultiScale(gray_face,1.1,4)
#     for (x,y,w,h) in face:
#         pic = pic[y:y+h,x:x+w]
#     '''cv.imshow("test",pic)
#     cv.waitKey(0)
#     cv.destroyAllWindows()'''
#     rect,pict =cv.imencode('.jpg',pic)
#     picture=pict.tobytes()
#     cursor=db.cursor()   
#     if user_type=='admin' :
#         sql=("update admins set image=%s where name='{n}'").format(n=name)
#     elif user_type=='student':
#         sql = ("update users set image=%s where name='{n}'").format(n=name)   
#     args = (picture, )       
#     cursor.execute(sql,args)
#     db.commit()

# def receive(name_face):
#     global data
#     cursor=db.cursor()
#     if usertype=='admin':
#         query1= ("SELECT image from admins where username='{n}' ").format(n=name_face)
#     elif usertype=='student':
#         query1= ("SELECT image from users where username='{n}' ").format(n=name_face)
#     cursor.execute(query1)
#     data=cursor.fetchall()
#     im = Image.open(BytesIO(data[0][0]))
#     #im1=im.convert("RGB")
#     #img=np.array(im1.getdata())
#     opencvImage = cv.cvtColor(np.array(im), cv.COLOR_RGB2BGR)
    
#     return opencvImage