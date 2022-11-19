from deepface import DeepFace

class FaceVerify:

    def match_face(db_image,captured_image):
        model_result=DeepFace.verify(img1_path = db_image, img2_path =captured_image,enforce_detection=False)
        print(model_result)
        return model_result
        
