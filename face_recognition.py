import cv2
from main import MainThread

def face_recog():

    # Local Binary Patterns Histogram
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')  # load trained model
    cascadePath = "haarcascade_frontalface_default.xml"

    # initializing haar cascade for object detection approach
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX  # denotes the fonr type

    id = 2  # number of people you want to limit recognition for login

    # names,leave first empty, bcz counter starts from 0
    names = ['', 'Master User']

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # cv2.CAP_DSHOW is to remove warning
    cam.set(3, 640)  # set vdo Frame Width
    cam.set(4, 480)  # set vdo Frame Height

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:
        ret, img = cam.read()  # read the frames using above created object
        # the function converts img to grayscale
        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:
            # used to draw a rectangle around the detected face
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # to predict to person to be logged in on every single image which is being iterated
            id, accuracy = recognizer.predict(converted_image[y:y+h, x:x+w])

            if accuracy < 60:
                id = names[id]
                accuracy = "  {0}%".format(round(100-accuracy))
                # MainThread.TaskExecution()
            else:
                id = "Unknown"
                accuracy = "  {0}%".format(round(100-accuracy))
                break

            cv2.putText(img, str(id), (x+5, y-5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy), (x+5, y+h-5),
                        font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff
        if k == 27:  # Press esc to exit the vdo
            break

    # Do cleanup
    print("Thank You for using this program")
    cam.release()
    cv2.destroyAllWindows()