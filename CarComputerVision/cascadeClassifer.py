import cv2
import numpy as np




class Classifier:

        # haar cascades for image recognition

        _face_cascade = cv2.CascadeClassifier('/Users/morgan/Desktop/COMPUTER SCI Coursework/CarComputerVision/classifiers/haarcascade_frontalface_default.xml')
        _eye_cascade = cv2.CascadeClassifier('/Users/morgan/Desktop/COMPUTER SCI Coursework/CarComputerVision/classifiers/haarcascade_eye.xml')

        def find_face(self, _img):
            # print(_img)
            img_bw = cv2.cvtColor(_img, cv2.COLOR_RGB2GRAY)
            faces = Classifier._face_cascade.detectMultiScale(img_bw, 1.3, 5)

            face = None  # declare face as null value (not entirely necessary but for peace of mind and consistency)

            # filter out additional faces and look for the largest detected face (almost always the real face)

            if len(faces) > 1:
                biggest = (0, 0, 0, 0)

                # compare the width of the different instances and if the width is bigger than the previous
                # instance, replace biggest with instance i
                for i in faces:
                    if i[3] > biggest[3]:
                        biggest = i

            elif len(faces) == 1:
                biggest = faces
            else:
                return None
            try:
                for (x, y, w, h) in biggest:
                    face = _img[y:y + h, x:x + w]
                return face
            except:
                return None

            # return faces # for testing and returning the portions for rectangle around face

        def find_eyes(self, _img):
            img_bw = cv2.cvtColor(_img, cv2.COLOR_RGB2GRAY)

            eyes = Classifier._eye_cascade.detectMultiScale(img_bw,1.3,5)

            height = np.size(img_bw, 0)  # get face frame height
            width = np.size(img_bw, 0)  # get face frame height

            left_eye = None
            right_eye = None

            for (x, y, w, h) in eyes:
                if y+h > height / 2:  # ignore eyes below haf the face
                    pass
                eye_center = x + w / 2  # get the eye center
                if eye_center < width * 0.5:
                        left_eye = _img[y:y + h, x:x + w]
                else:
                        right_eye = _img[y:y + h, x:x + w]

            return left_eye, right_eye

        def cut_eyebrows(self, img):  # identify areas where eyebrows would be and remove them in
            # order to prevent them affecting the blob detection
            height, width = img.shape[:2]
            eyebrow_h = int(height / 4)
            img = img[eyebrow_h:height, 0:width]

            return img

# Testing
if __name__ == "__main__":
    classifier = Classifier()
    img = cv2.imread("/Users/morgan/Desktop/COMPUTER SCI Coursework/CarComputerVision/test_images/IMG_0812.JPG")

    # cv2.imshow("eye", img)
    face = classifier.find_face(img)
    eyes = classifier.find_eyes(face)
    # gaussed = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)
    # cv2.imshow("eye", gaussed)
    cv2.imwrite("/Users/morgan/Desktop/COMPUTER SCI Coursework/CarComputerVision/test_images/eye_test_2.JPG", eyes[1])
    cv2.waitKey(0)
    cv2.destroyAllWindows()