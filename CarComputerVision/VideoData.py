import cv2

class VideoData:

    def __init__(self):
        pass
        self.frame = None
        self.face = None
        self.left_eye = None
        self.right_eye = None
        self.left_eye_threshold = None
        self.right_eye_threshold = None
        self.left_eye_threshold_direction = None
        self.right_eye_threshold_direction = None

    def set_frame(self, _frame):

        self.frame = _frame

    def get_frame(self):
        return self.frame

    def set_face(self, _frame):

        self.frame = _frame

    def get_face(self):
        return self.frame