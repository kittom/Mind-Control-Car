import cv2
from CarComputerVision.Blob import ImgProcessor
from CarComputerVision.cascadeClassifer import Classifier
from CarComputerVision.direction import DirectionManager
# from CarComputerVision.VideoData import VideoData

class EyeMotionLoop:
    classifier = Classifier()

    # class VideoData

    def __init__(self, camera_option=0):
        self.cap = cv2.VideoCapture(camera_option)
        self.processor = ImgProcessor()
        self.directionManager = DirectionManager(0.4, 0.25)
        self.prev_response = None

    def mainloop(self):

        while True:
            ret, frame = self.cap.read()
            if ret:

                face = self.classifier.find_face(frame)

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
                        keypoint_img, keypoints = [None, None], [None, None]
                        keypoint_img[0], keypoints[0] = self.processor.blob_process(thresholds[0])
                        keypoint_img[1], keypoints[1] = self.processor.blob_process(thresholds[1])
                        cv2.imshow("threshold 2", keypoint_img[0])
                        # if keypoint_img[0] is not None and keypoint_img[1] is not None:

                        direction = [None, None]

                        for i in (0, len(keypoints)-1):

                            if keypoints[i] is not None:
                                self.directionManager.calculate_thresholds(keypoint_img[i])
                                cv2.imshow(f"dm-{i+1}", self.directionManager.display(keypoint_img[i]))

                                direction[i] = self.directionManager.get_direction(keypoints[i])

                        if direction != [None, None]:

                            response = self.directionManager.get_direction_logic(direction)

                            if response != self.prev_response:
                                self.prev_response = response
                                print(response)


            else:
                pass
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":

    video = EyeMotionLoop()
    video.mainloop()
