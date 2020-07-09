import cv2
import numpy as np



class Classifier:

        # haar cascades for image recognition

        _face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_default.xml')
        _eye_cascade = cv2.CascadeClassifier('classifiers/haarcascade_eye.xml')

        def find_faces(self):
            img_bw = cv2.cvtColor(self,cv2.COLOR_RGB2GRAY)
            faces = Classifier._face_cascade.detectMultiScale(img_bw,1.3,5)

            face = None  # declare face as null value (not entirely necessary but for peace of mind and consistency)

            # filter out additional faces and look for the largest detected face (almost always the real face)

            if len(faces) > 1:
                biggest = (0, 0, 0, 0)

                # compare the width of the different instances and if the width is bigger than the previous
                # instance, replace biggest with instance i
                for i in faces:
                    if i[3] > biggest[3]:  biggest = i

            elif len(faces) == 1:
                biggest = faces
            else:
                return None

            for (x, y, w, h) in biggest:
                face = self[y:y + h, x:x + w]
            return face
            # return faces # for testing and returning the portions for rectangle around face

        def find_eyes(self):
            img_bw = cv2.cvtColor(self, cv2.COLOR_RGB2GRAY)
            eyes = Classifier._eye_cascade.detectMultiScale(img_bw,1.3,5)
            height = np.size(img_bw, 0)  # get face frame height
            width = np.size(img_bw, 0)  # get face frame height

            left_eye = None
            right_eye = None

            for (x, y, w, h) in eyes:
                if y+h > height/2: # pass if the eye is at the bottom
                    pass
                eye_center = x + w / 2  # get the eye center
                if eye_center < width * 0.5:
                        left_eye = self[y:y + h, x:x + w]
                else:
                        right_eye = self[y:y + h, x:x + w]

            return left_eye, right_eye
