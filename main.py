from kivy.app import App
from kivy.uix.widget import Widget
import cv2
import face_recognition
import mysql.connector
import shutil
from datetime import datetime
import os

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="faces1",
    password="Shanthini123456*",
    auth_plugin='mysql_native_password',
    database="faces"
)
class attendance1(Widget):


    pass

class attendance2(App):
    def build(self):
        known_face_encodings = []
        known_face_names = []
        known_persons = []
        known_persons1 = []
        known_persons2 = []

        known_person1 = "./shamu.jpg"
        known_person2 = "./Ganeshan.png"
        known_person3 = "./miru.png"
        known_person4 = "./kannan.png"
        known_person5 = "./Madhesh.jpg"
        known_person6 = "./Arun.png"
        known_person7 = "./sathya.png"
        known_person8 = "./abinaya.png"

        known_person1_image = face_recognition.load_image_file("shamu.jpg")
        known_person2_image = face_recognition.load_image_file("Ganeshan.png")
        known_person3_image = face_recognition.load_image_file("miru.png")
        known_person4_image = face_recognition.load_image_file("kannan.png")
        known_person5_image = face_recognition.load_image_file("Madhesh.jpg")
        known_person6_image = face_recognition.load_image_file("Arun.png")
        known_person7_image = face_recognition.load_image_file("sathya.png")
        known_person8_image = face_recognition.load_image_file("abinaya.png")

        known_person11 = "/shamu.jpg"
        known_person21 = "/Ganeshan.png"
        known_person31 = "/miru.png"
        known_person41 = "/kannan.png"
        known_person51 = "/Madhesh.jpg"
        known_person61 = "/Arun.png"
        known_person71 = "/sathya.png"
        known_person81 = "/abinaya.png"

        known_person12 = "shamu"
        known_person22 = "Ganeshan"
        known_person32 = "miru"
        known_person42 = "kannan"
        known_person52 = "Madhesh"
        known_person62 = "Arun"
        known_person72 = "sathya"
        known_person82 = "abinaya"

        known_persons.append(known_person1)
        known_persons.append(known_person2)
        known_persons.append(known_person3)
        known_persons.append(known_person4)
        known_persons.append(known_person5)
        known_persons.append(known_person6)
        known_persons.append(known_person7)
        known_persons.append(known_person8)

        known_persons1.append(known_person11)
        known_persons1.append(known_person21)
        known_persons1.append(known_person31)
        known_persons1.append(known_person41)
        known_persons1.append(known_person51)
        known_persons1.append(known_person61)
        known_persons1.append(known_person71)
        known_persons1.append(known_person81)

        known_persons2.append(known_person12)
        known_persons2.append(known_person22)
        known_persons2.append(known_person32)
        known_persons2.append(known_person42)
        known_persons2.append(known_person52)
        known_persons2.append(known_person62)
        known_persons2.append(known_person72)
        known_persons2.append(known_person82)

        # known_person1_image_o = face_recognition.load_image_file("shamu.jpg")
        # known_person2_image_o = face_recognition.load_image_file("Ganeshan.png")
        # known_person3_image_o = face_recognition.load_image_file("miru.png")
        # known_person4_image_o = face_recognition.load_image_file("kannan.png")
        # known_person5_image_o=face_recognition.load_image_file("Madhesh.jpg")

        # known_person1_image=cv2.cvtColor(known_person1_image_o,cv2.COLOR_BGR2RGB)
        # known_person2_image=cv2.cvtColor(known_person2_image_o,cv2.COLOR_BGR2RGB)
        # known_person3_image=cv2.cvtColor(known_person3_image_o,cv2.COLOR_BGR2RGB)
        # known_person4_image=cv2.cvtColor(known_person4_image_o,cv2.COLOR_BGR2RGB)
        # known_person5_image=cv2.cvtColor(known_person5_image_o,cv2.COLOR_BGR2RGB)
        known_person1_encoding = face_recognition.face_encodings(known_person1_image)[0]
        known_person2_encoding = face_recognition.face_encodings(known_person2_image)[0]

        known_person3_encoding = face_recognition.face_encodings(known_person3_image)[0]

        known_person4_encoding = face_recognition.face_encodings(known_person4_image)[0]

        known_person5_encoding = face_recognition.face_encodings(known_person5_image)[0]
        known_person6_encoding = face_recognition.face_encodings(known_person6_image)[0]
        known_person7_encoding = face_recognition.face_encodings(known_person7_image)[0]
        known_person8_encoding = face_recognition.face_encodings(known_person8_image)[0]

        known_face_encodings.append(known_person1_encoding)
        known_face_encodings.append(known_person2_encoding)

        known_face_encodings.append(known_person3_encoding)

        known_face_encodings.append(known_person4_encoding)

        known_face_encodings.append(known_person5_encoding)
        known_face_encodings.append(known_person6_encoding)
        known_face_encodings.append(known_person7_encoding)
        known_face_encodings.append(known_person8_encoding)

        known_face_names.append("Shanmuga Lakshmi Devaraj")
        known_face_names.append("Ganeshan Mahalingam")
        known_face_names.append("Miru")
        known_face_names.append("Kannan")
        known_face_names.append("Madhesh")
        known_face_names.append("Arun M")
        known_face_names.append("Sathya")
        known_face_names.append("Abinaya")

        video = cv2.VideoCapture(0)
        address = "http://192.168.172.199:8080/video"
        video.open(address)

        if not video.isOpened():
            print("Cannot open camera")
            exit()
        while True:
            # Capture frame-by-frame
            ret, frame = video.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            # frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown Person"
                folder="./folder"

                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                    filetocopy = known_persons[first_match_index]
                    filetocopy1 = known_persons1[first_match_index]
                    pers = known_persons2[first_match_index]
                    x = folder + "/" + filetocopy1
                    if not os.path.exists(x):



                        if name is not None:

                            shutil.copy(filetocopy, folder)
                            pers = known_persons2[first_match_index]
                            form_t = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

                            f1 = os.path.split(x)[0] + '/' + pers + form_t + os.path.splitext(x)[1]
                            cv2.imwrite(f"{folder}/idx.png", frame)
                            x=folder+"/idx.png"
                            os.rename(x, f1)

                            mycursor=mydb.cursor()
                            t=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            mycursor.execute("insert into face1 values(%s,%s)",(name,t))
                            mydb.commit()

                cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 0, 0), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

                #

            # Display the resulting frame
            cv2.imshow('frame', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        mydb.close
        video.release()
        cv2.destroyAllWindows()
        return attendance1()

attendance2().run()
