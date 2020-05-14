import imp
imp.find_module("cv2")
import cv2
import numpy as np
import face_recognition
#recognizer = cv2.createLBPHFaceRecognizer()
#recognizer.load("Enter fulll location of trainer.yml within quotes")
faceDetect = cv2.CascadeClassifier("Enter fulll location of harrcascade_frontalface_alt2.xml within quotes")
my_image = face_recognition.load_image_file("Enter fulll location of image(jpg) within quotes")
my_face_encoding = face_recognition.face_encodings(my_image)[0]
known_face_encodings = [
    my_face_encoding
]
known_face_names = [
    "Your name"
]
c=[]
d=[]
name=""
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
access=0
while 1:
    a=raw_input("Enter 1 to start (Press q after starting to exit): ")
    if a=='1':
        video_capture = cv2.VideoCapture(0)
        face_locations = []
        face_encodings = []
        face_names = [] 
        process_this_frame = True
        access=0
        thief=0
        while True:
            ret, frame = video_capture.read()

            
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            
            rgb_small_frame = small_frame[:, :, ::-1]

            
            if process_this_frame:
                
            	face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"
                    if not True in matches:
                        thief+=1
                        access=0
                    
                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]
                        access+=1        
                
                    face_names.append(name)

            process_this_frame = not process_this_frame
            
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

               
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0,255, 0), 1)
 	cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
video_capture.release()
cv2.destroyAllWindows()
