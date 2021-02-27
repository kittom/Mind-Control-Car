import cv2
# import facialRecognition
from CarComputerVision.cascadeClassifer import Classifier

class BlobDetector:

    params = cv2.SimpleBlobDetector_Params()  # create a new list of parameters for blob detector
    params.filterByArea = True
    params.maxArea = 1500

    blob_detector = cv2.SimpleBlobDetector_create(params)  # create blob detector and assign parameter list


    def blob_process(self, img, threshold):

        gray_frame = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) # turn image into bw version
        ret, img = cv2.threshold(gray_frame, threshold, 255, cv2.THRESH_BINARY) # create threshold image
        img = cv2.erode(img, None, iterations=2)  # 1
        img = cv2.dilate(img, None, iterations=4)  # 2
        img = cv2.medianBlur(img, 5)  # 3
        # cv2.imshow("threshold image", img)
        keypoints = self.blob_detector.detect(img)

        # check if there is more than one keypoint and keep the largest.
        if len(keypoints) > 1:

            kp = keypoints[0]
            for k in keypoints[1:]:
                if k.size > kp.size:
                    kp = k
            return kp, img

        return keypoints, img


# Testing

if __name__ == "__main__":
    classifier = Classifier()
    blobDetector = BlobDetector()

    img = cv2.imread("/Users/morgan/Desktop/Mind-Control-Car/CarComputerVision/test_images/IMG_0812.JPG")

    eyes = classifier.find_eyes(classifier.find_face(img))
    map(classifier.cut_eyebrows, eyes)
    print(len(eyes))
    cv2.imshow("eye", eyes[0])
    keypoints = blobDetector.blob_process(eyes[0],51)
    print(keypoints)
    eye1 = cv2.drawKeypoints(eyes[0], keypoints[0], eyes[0], (0, 0, 255),
                             cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    eye2 = cv2.drawKeypoints(eyes[1], keypoints[1], eyes[1], (0, 0, 255),
                             cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("keypoints eye", eyes[0])
    cv2.waitKey(0)
    cv2.destroyAllWindows()