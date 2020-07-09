import cv2
from facialRecognition import Classifier



def cut_eyebrows(img):
    height, width = img.shape[:2]
    eyebrow_h = int(height / 4)
    img = img[eyebrow_h:height, 0:width]

    return img


def blob_process(img, detector):

    gray_frame = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, img = cv2.threshold(gray_frame, 42, 255, cv2.THRESH_BINARY)
    keypoints = detector.detect(img)

    return keypoints


params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.maxArea = 1500
blob_detector = cv2.SimpleBlobDetector_create(params)

classifier = Classifier



img = cv2.imread("test_images/IMG_0812.JPG")


eyes = classifier.find_eyes(classifier.find_faces(img))

eye = cut_eyebrows(eyes[0])

keypoints = blob_process(eye, blob_detector)

eye_kp = cv2.drawKeypoints(eye, keypoints, eye, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("bw",eye_kp)

cv2.waitKey(0)
cv2.destroyAllWindows()