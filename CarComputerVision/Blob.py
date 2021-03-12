import cv2


class ImgProcessor:

    def __init__(self, blob_filter_by_area=True, blob_max_area=1500):

        params = cv2.SimpleBlobDetector_Params()  # create a new list of parameters for the blob detector
        params.filterByArea = blob_filter_by_area
        params.maxArea = blob_max_area

        self.blob_detector = cv2.SimpleBlobDetector_create(params)  # create blob detector and assign parameters

    def blob_process(self, _img, output_img=None):

        key_points = self.blob_detector.detect(_img)


        kp = [cv2.KeyPoint(None, 0.0, None)]
        if len(key_points) >= 2:
            for k in key_points:
                if kp[0].size < k.size:
                    kp[0] = k
        elif len(key_points) == 1:
            kp[0] = key_points[0]

        if output_img:
            blob_img = cv2.drawKeypoints(_img, kp, output_img, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        else:
            blob_img = cv2.drawKeypoints(_img, kp, _img, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        return blob_img, kp[0]

    @staticmethod
    def threshold_process(color_img, _threshold, erode_iterations=2, dilate_iteration=4, median_blur=5):

        gray_frame = cv2.cvtColor(color_img, cv2.COLOR_RGB2GRAY)  # turn image into bw version
        ret, th_img = cv2.threshold(gray_frame, _threshold, 255, cv2.THRESH_BINARY)  # create threshold image
        th_img = cv2.erode(th_img, None, iterations=erode_iterations)  # 1
        th_img = cv2.dilate(th_img, None, iterations=dilate_iteration)  # 2
        th_img = cv2.medianBlur(th_img, median_blur)
        return th_img


# main testing code.
if __name__ == "__main__":

    ImgProcessor = ImgProcessor()

    img = cv2.imread("/Users/morgan/Desktop/Mind-Control-Car/CarComputerVision/test_images/blob_detection_1.png")
    threshold_img = ImgProcessor.threshold_process(img, 51)
    cv2.imshow("threshold", threshold_img)
    blob, kp = ImgProcessor.blob_process(threshold_img)
    cv2.imshow("Blob", blob)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# img processing code

# if __name__ == "__main__":
#     ImgProcessor = ImgProcessor()
#     img = cv2.imread("/Users/morgan/Desktop/Mind-Control-Car/CarComputerVision/test_images/eye_test.JPG")
#     threshold_img = ImgProcessor.threshold_process(img, 51)
#     cv2.imshow("original", img)
#     cv2.imshow("threshold", threshold_img)
#
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
