from deepface import DeepFace

class FaceVerify:

    def match_face(db_image,realtime_iamge)-> bool:
        # /home/sahil/Downloads/1.jpg','/home/sahil/Downloads/2.jpg'
        # temp=DeepFace.verify(img1_path = db_image, img2_path =realtime_iamge,enforce_detection=False)
        model_name = "VGG-Face"
        model = DeepFace.build_model(model_name)
        temp=DeepFace.verify(img1_path = '/home/sahil/Downloads/1.jpg', img2_path ='/home/sahil/Downloads/2.jpg',enforce_detection=False)
        print(temp)
        return temp

FaceVerify.match_face(1,2)