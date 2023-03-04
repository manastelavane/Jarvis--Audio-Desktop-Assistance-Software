import cv2
import numpy as np
from PIL import Image #pillow package
import os

def train_model():
    #newpath = r"C:\\Users\\santo\\OneDrive\\Documents\\PythonFiles\\Python_Projects\\Face_login\\trainer"
    newpath = r"trainer"
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    path='samples' #path of the samples which were taken

    recognizer=cv2.face.LBPHFaceRecognizer_create() #Local Binary Patterns Hisstogram
    detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def Images_And_Labels(path): # function to fetch the images and labels
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
        faceSamples=[]
        ids=[]
        
        for imagePath in imagePaths: #to iterate particular image path
            gray_img=Image.open(imagePath).convert('L') #convert it to grayscale
            img_arr=np.array(gray_img,'uint8') #creating an array

            id=int(os.path.split(imagePath)[-1].split(".")[1])
            faces=detector.detectMultiScale(img_arr)

            for(x,y,w,h) in faces:
                faceSamples.append(img_arr[y:y+h,x:x+w])
                ids.append(id)

        return faceSamples, ids

    print("Training faces. This will take a few moments...")

    faces, ids=Images_And_Labels(path)
    recognizer.train(faces,np.array(ids))

    recognizer.write('trainer/trainer.yml') #Save the trained as trainer.yml
    print("Model Trained. Now we can recognize youe face for future logins.")