import cv2
from CarComputerVision.Blob import ImgProcessor
from CarComputerVision.cascadeClassifer import Classifier

class Video:
    classifier = Classifier()

    keypoints = [[], []]

    # class VideoData

    def __init__(self, camera_option=0):
        self.cap = cv2.VideoCapture(camera_option)
        self.processor = ImgProcessor()

    def mainloop(self):
        # cv2.namedWindow('image')
        # cv2.namedWindow('image1')
        # cv2.namedWindow('image2')
        # cv2.namedWindow('image3')
        #
        # cv2.createTrackbar('threshold-1', 'image', 0, 255, lambda: None)
        # cv2.createTrackbar('threshold-2', 'image1', 0, 255, lambda: None)

        while True:
            ret, frame = self.cap.read()
            if ret:
                face = self.classifier.find_face(frame)
                # print(face)

                if face is not None:
                    cv2.imshow("face", face)
                    eyes = self.classifier.find_eyes(face)

                    if eyes[0] is not None and eyes[1] is not None:
                        map(self.classifier.cut_eyebrows, eyes)
                        cv2.imshow("left eye", eyes[0])
                        cv2.imshow("Right eye", eyes[1])

                        thresholds = [self.processor.threshold_process(eyes[0], 74),
                                      self.processor.threshold_process(eyes[1], 74)]

                        cv2.imshow("threshold 1", thresholds[0])
                        cv2.imshow("threshold 2", thresholds[1])
                        keypoint_img,keypoint = [],[]
                        keypoint_img = self.processor.blob_process(thresholds[0])
                        # keypoint_img[1], keypoint[1], = self.processor.blob_process(thresholds[1])
                        cv2.imshow("threshold 2", keypoint_img)

                else:
                    pass

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

                # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":

    video = Video()
    video.mainloop()
