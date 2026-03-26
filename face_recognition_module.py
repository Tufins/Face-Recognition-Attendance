import face_recognition
import cv2
import os
import numpy as np

class FaceRecognizer:

    def __init__(self, image_path):
        self.image_path = image_path
        self.images = []
        self.classNames = []
        self.encodeList = []

    def load_images(self):
        myList = os.listdir(self.image_path)

        for cl in myList:
            img = cv2.imread(f'{self.image_path}/{cl}')
            self.images.append(img)
            self.classNames.append(os.path.splitext(cl)[0])

    def encode_faces(self):
        for img in self.images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            self.encodeList.append(encode)

    def recognize_faces(self, frame):
        imgS = cv2.resize(frame, (0,0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        faces = face_recognition.face_locations(imgS)
        encodes = face_recognition.face_encodings(imgS, faces)

        results = []

        for encodeFace, faceLoc in zip(encodes, faces):
            matches = face_recognition.compare_faces(self.encodeList, encodeFace)
            faceDis = face_recognition.face_distance(self.encodeList, encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = self.classNames[matchIndex].upper()
                results.append((name, faceLoc))

        return results