import cv2
from facialRecognition import Classifier


class BlobDetector:

    params = cv2.SimpleBlobDetector_Params()  # create a new list of parameters for blob detector
    params.filterByArea = True
    params.maxArea = 1500

    blob_detector = cv2.SimpleBlobDetector_create(params)  # create blob detector and assign parameter list

    def cut_eyebrows(self, img): # identify areas where eyebrows would be and remove them in
                            # order to prevent them affecting the blob detection
        height, width = img.shape[:2]
        eyebrow_h = int(height / 4)
        img = img[eyebrow_h:height, 0:width]

        return img

    def blob_process(self, img):

        gray_frame = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) # turn image into bw version
        ret, img = cv2.threshold(gray_frame, 30, 255, cv2.THRESH_BINARY) # create threshold image
        img = cv2.erode(img, None, iterations=2)  # 1
        img = cv2.dilate(img, None, iterations=4)  # 2
        img = cv2.medianBlur(img, 7)  # 3
        cv2.imshow("threshold image", img)
        keypoints = self.blob_detector.detect(img)

        return keypoints



# classifier = Classifier
#
# # TESTING
#
# img = cv2.imread("test_images/IMG_0812.JPG")  # initial image
# img_display = cv2.imread("test_images/road_test_image.jpg")
# eyes = classifier.find_eyes(classifier.find_face(img)) # find the eyes within the face of img
#
# eye = cut_eyebrows(eyes[1]) # for sake of testing only using one eye
#
# cv2.imshow("img",eye) # display image without keypoints circled
#
# img_blobs = BlobDetector.blob_process(eye, blob_detector)  # find keypoints
#
# print(img_blobs) # check to see what keypoints have been found
#
# # draw circles according to where keypoint(s) were
# cv2.drawKeypoints(img_display,img_blobs,img_display, (0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# #
#
# cv2.imshow("blobs detected",img_display) # display same image but with circles on keypoints
#
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()