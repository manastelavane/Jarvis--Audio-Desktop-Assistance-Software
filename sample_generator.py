import cv2
import os
from login import Login_Window

def take_samples():

    # newpath = r"C:\\Users\\santo\\OneDrive\\Documents\\PythonFiles\\Python_Projects\\Face_login\\samples"
    newpath = r"samples"
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # capturing vdo through Laptop webcam
    cam.set(3, 640)  # setting vdo Frame Width
    cam.set(4, 480)  # setting vdo Frame Height

    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Haar Cascade classifier is used as an effective Object Detection approach

    face_id = 1
    # Use integer ID for every new face(0,1,2,3,....)

    print("Taking samples, look at camera....")
    count = 0  # initializing sampling face count

    while True:
        ret, img = cam.read()  # read the faces using the above created object
        # converting img into grayscale
        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(converted_image, 1.3, 5)

        for (x, y, w, h) in faces:
            # drawing rectangle around detected face
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            count += 1

            cv2.imwrite("samples/face."+str(face_id)+"."+str(count) +
                        ".jpg", converted_image[y:y+h, x:x+w])
            # to capture and save imgs into the dataset folder

            cv2.imshow('image', img)  # used to display img in window

        k = cv2.waitKey(100) & 0xff  # Waits for a pressed key
        if k == 27:  # press esc key to stop
            break
        elif count >= 50:  # taking 50 samples (More samples give more accuracy)
            break

    print("Samples taken successfully. Now closing the program")
    cam.release()
    cv2.destroyAllWindows()