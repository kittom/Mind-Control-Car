import cv2
from CarComputerVision.Blob import ImgProcessor
from CarComputerVision.cascadeClassifer import Classifier
from CarComputerVision.direction import DirectionManager
from BrainWaveReader.FileManager import FileManager


class EyeMotionLoop:


    class VideoData:

        def __init__(self):


            self.frame = None
            self.face = None
            self.left_eye = None
            self.right_eye = None
            self.left_eye_threshold = None
            self.right_eye_threshold = None
            self.left_eye_blob = None
            self.right_eye_blob = None
            self.left_eye_threshold_direction = None
            self.right_eye_threshold_direction = None
            self.direction = None
            self.velocity = None

        def set_frame(self, _img):
            self.frame = _img

        def get_frame(self):
            return self.frame

        def set_face(self, _img):
            self.face = _img

        def get_face(self):
            return self.face

        def set_left_eye(self, _img):
            self.left_eye = _img

        def get_left_eye(self):
            return self.left_eye

        def set_right_eye(self, _img):
            self.right_eye = _img

        def get_right_eye(self):
            return self.right_eye

        def set_left_eye_threshold(self, _img):
            self.left_eye_threshold = _img

        def get_left_eye_threshold(self):
            return self.left_eye_threshold

        def set_right_eye_threshold(self, _img):
            self.right_eye_threshold = _img

        def get_right_eye_threshold(self):
            return self.right_eye_threshold

        def set_left_eye_blob(self, _img):
            self.left_eye_blob = _img

        def get_left_eye_blob(self):
            return self.left_eye_blob

        def set_right_eye_blob(self, _img):
            self.right_eye_blob = _img

        def get_right_eye_blob(self):
            return self.right_eye_blob

        def set_left_eye_threshold_direction_display(self, _img):
            self.left_eye_threshold_direction = _img

        def get_left_eye_threshold_direction_display(self):
            return self.left_eye_threshold_direction

        def set_right_eye_threshold_direction_display(self, _img):
            self.right_eye_threshold_direction = _img

        def get_right_eye_threshold_direction_display(self):
            return self.right_eye_threshold_direction

        def set_direction(self, _data):
            self.direction = _data

        def get_direction(self):
            return self.direction

        def set_velocity(self, _velocity):
            self.velocity = _velocity

        def get_velocity(self):
            return self.velocity

    classifier = Classifier()
    processor = ImgProcessor()


    def __init__(self):
        self.dt = self.VideoData()
        self.directionManager = DirectionManager(0.4, 0.25)
        self.file_manager = FileManager()
        self.prev_response = None

    def get_data(self, frame, threshold_l, threshold_r, _left, _right):

        self.dt.set_frame(cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA))
        face = self.classifier.find_face(frame)

        if face is not None:

            self.dt.set_face(cv2.cvtColor(face, cv2.COLOR_BGR2RGBA))

            eyes = self.classifier.find_eyes(face)

            if eyes[0] is not None and eyes[1] is not None:

                map(self.classifier.cut_eyebrows, eyes)
                self.dt.set_right_eye(cv2.cvtColor(eyes[0], cv2.COLOR_BGR2RGBA))
                self.dt.set_left_eye(cv2.cvtColor(eyes[1], cv2.COLOR_BGR2RGBA))

                thresholds = [self.processor.threshold_process(eyes[0], threshold_r),
                              self.processor.threshold_process(eyes[1], threshold_l)]

                self.dt.set_right_eye_threshold(thresholds[0])
                self.dt.set_left_eye_threshold(thresholds[1])

                keypoint_img, keypoints = [None, None], [None, None]
                keypoint_img[0], keypoints[0] = self.processor.blob_process(thresholds[0])
                keypoint_img[1], keypoints[1] = self.processor.blob_process(thresholds[1])

                direction = [None, None]

                if keypoints[1] is not None:
                    self.directionManager.set_left(_left), self.directionManager.set_right(_right)

                    self.directionManager.calculate_thresholds(keypoint_img[1])
                    self.dt.set_left_eye_threshold_direction_display(cv2.cvtColor(self.directionManager.display(
                        keypoint_img[1]), cv2.COLOR_BGR2RGBA))
                    # cv2.imshow("dm-1}", self.directionManager.display(keypoint_img[1]))
                    direction[1] = self.directionManager.get_direction(keypoints[1])

                if keypoints[0] is not None:
                    self.directionManager.calculate_thresholds(keypoint_img[0])
                    self.dt.set_right_eye_threshold_direction_display(cv2.cvtColor(self.directionManager.display(
                        keypoint_img[0]), cv2.COLOR_BGR2RGBA))
                    # cv2.imshow("dm-0", self.directionManager.display(keypoint_img[0]))
                    direction[0] = self.directionManager.get_direction(keypoints[0])

                if direction != [None, None]:

                    response = self.directionManager.get_direction_logic(direction)

                    if response != self.prev_response:
                        self.dt.set_direction(response)
                        self.prev_response = response
        self.dt.set_velocity(self.file_manager.get_dt())
        return self.dt


if __name__ == "__main__":

    logic = EyeMotionLoop()

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        if ret:

            dt = logic.get_data(frame, 0, 0, 0, 0)

            print(dt.get_velocity())

            # dt = logic.mainloop(dt)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
