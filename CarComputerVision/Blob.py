import cv2
# import facialRecognition
from CarComputerVision.cascadeClassifer import Classifier

class ImgProcessor:
    def __init__(self):

        params = cv2.SimpleBlobDetector_Params()  # create a new list of parameters for blob detector
        params.filterByArea = True
        params.maxArea = 1500

        self.blob_detector = cv2.SimpleBlobDetector_create(params)  # create blob detector and assign parameter list

    def blob_process(self, img):

        keypoints = self.blob_detector.detect(img)
        print(keypoints)

        # # check if there is more than one keypoint and keep the largest.
        # kp = []
        # print(keypoints)
        # if len(keypoints) > 1:
        #     kp = keypoints[0]
        #     for k in keypoints[1:]:
        #         if k.size > kp.size:
        #             kp[0] = [k]
        # else:
        #     kp[0] = [keypoints]
        #
        # print(kp)

        # blob_img = img
        blob_img = cv2.drawKeypoints(img, keypoints, img, (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        return blob_img

    def threshold_process(self, _img, _threshold):
        gray_frame = cv2.cvtColor(_img, cv2.COLOR_RGB2GRAY) # turn image into bw version
        ret, img = cv2.threshold(gray_frame, _threshold, 255, cv2.THRESH_BINARY) # create threshold image
        img = cv2.erode(img, None, iterations=2)  # 1
        img = cv2.dilate(img, None, iterations=4)  # 2
        img = cv2.medianBlur(img, 5)
        return img



# Testing

# if __name__ == "__main__":
#     classifier = Classifier()
#     blobDetector = BlobDetector()
#
#     img = cv2.imread("/Users/morgan/Desktop/Mind-Control-Car/CarComputerVision/test_images/IMG_0812.JPG")
#
#     eyes = classifier.find_eyes(classifier.find_face(img))
#     map(classifier.cut_eyebrows, eyes)
#     print(len(eyes))
#     cv2.imshow("eye", eyes[0])
#
#     keypoints1, img_1 = blobDetector.blob_process(eyes[1],51)
#     # keypoints = [blobDetector.blob_process(eyes[0],51), blobDetector.blob_process(eyes[0],51)]
#     # print(keypoints[1])
#     print(len(keypoints1))
#
#     eye1 = cv2.drawKeypoints(eyes[1], keypoints1, eyes[1], (0, 0, 255))
#     # eye2 = cv2.drawKeypoints(eyes[1], keypoints[1], eyes[1], (0, 0, 255))
#     cv2.imshow("keypoints eye", eye1)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

if __name__ == "__main__":
    classifier = Classifier()
    ImgProcessor = ImgProcessor()

    img = cv2.imread("/Users/morgan/Desktop/Mind-Control-Car/CarComputerVision/test_images/blob_detection_1.png")
    threshold_img = ImgProcessor.threshold_process(img, 51)
    cv2.imshow("threshold", threshold_img)
    blob = ImgProcessor.blob_process(threshold_img)
    cv2.imshow("Blob", blob)


    cv2.waitKey(0)
    cv2.destroyAllWindows()