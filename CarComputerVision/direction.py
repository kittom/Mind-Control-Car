import cv2
from CarComputerVision.Blob import ImgProcessor

class DirectionManager:
    def __init__(self, left, right):

        self.left = left
        self.right = right
        self.left_width = None
        self.right_width = None
        self.height = None

    def calculate_thresholds(self, _img):
        width, self.height, _ = _img.shape
        self.left_width = int(width * self.left)

        self.right_width = int(width * (1 - self.right))

        return self.left_width, self.right_width

    def display(self, _img):

        left_start_point, left_end_point = (self.left_width, 0), (self.left_width, self.height)
        right_start_point, right_end_point = (self.right_width, 0), (self.right_width, self.height)

        cv2.line(_img, left_start_point, left_end_point, (0, 0, 255), 1)
        cv2.line(_img, right_start_point, right_end_point, (0, 0, 255), 1)
        return _img

    def get_direction(self, keypoint):

        x_val = int(keypoint.pt[0])

        if x_val == 0.0:
            return None
        elif x_val <= self.left_width:
            return "left"

        elif x_val >= self.right_width:
            return "right"

        elif x_val > self.left_width and x_val < self.right_width:
            return "centre"
        else:
            return None

    @staticmethod
    def get_direction_logic(directions):

        if directions == ["left", "centre"] or directions == ["centre", "left"] or directions == ["left", "left"]:
            return "left"
        elif directions == ["right", "centre"] or directions == ["centre", "right"] or directions == ["right", "right"]:
            return "right"
        else:
            return "centre"


if __name__ == "__main__":
    dm = DirectionManager(0.4, 0.25)
    processor = ImgProcessor()
    img = cv2.imread("/Users/morgan/Desktop/Mind-Control-Car/CarComputerVision/test_images/blob_detection_1.png")
    threshold_img = ImgProcessor.threshold_process(img, 51)
    cv2.imshow("threshold", threshold_img)

    blob, kp = processor.blob_process(threshold_img)

    cv2.imshow("Blob", blob)
    #
    dm.calculate_thresholds(blob)
    kp2 = [cv2.KeyPoint(None, 0.0, None)]
    # print(kp2[0].pt)

    print(dm.get_direction(kp2[0]))
    display = dm.display(blob)
    #
    cv2.imshow("display", display)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
