from CarComputerVision.vidcap import EyeMotionLoop
from CarComputerVision.VideoData import VideoData
import cv2

dt = VideoData()
logic = EyeMotionLoop()

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if ret:

        dt.set_frame(frame)

        cv2.imshow("frame", dt.get_frame())

        dt = logic.mainloop(dt)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # When everything done, release the capture

cap.release()
cv2.destroyAllWindows()