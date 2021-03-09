import cv2
from CarComputerVision.Blob import ImgProcessor
from CarComputerVision.cascadeClassifer import Classifier

# better way of doing this where the loop sorrounds the returns and the UI is seperate
class Video:

    cap = cv2.VideoCapture(0)
    classifier = Classifier()
    blobDetector = ImgProcessor()
    keypoints = [[],[]]

    def mainloop(self):
        cv2.namedWindow('image')
        cv2.namedWindow('image1')
        cv2.namedWindow('image2')
        cv2.namedWindow('image3')

        cv2.createTrackbar('threshold-1', 'image', 0, 255, lambda: None)
        cv2.createTrackbar('threshold-2', 'image1', 0, 255, lambda: None)
        
        while True:
            # Capture frame-by-frame
            ret, frame = self.cap.read()

            # Our operations on the frame come here
            if ret:
                face = self.classifier.find_face(frame)

                try:
                    eyes = self.classifier.find_eyes(face)
                    # print(cv2.getTrackbarPos("threshold-2", "image1"))
                    try:
                        _threshold = [cv2.getTrackbarPos("threshold-1", "image"), cv2.getTrackbarPos("threshold-2", "image1")]
                    except:
                        _threshold = [0,0]
                    # print(_threshold)
                    # print(_threshold[0], _threshold[1])

                    map(self.classifier.cut_eyebrows, eyes)
                    cv2.imshow("image", eyes[0])
                    cv2.imshow("image1", eyes[1])
                    img=[None, None]

                    self.keypoints[0], img[0] = self.blobDetector.blob_process(eyes[0], _threshold[0])

                    self.keypoints[1], img[1] = self.blobDetector.blob_process(eyes[1], _threshold[1])
                    # print(self.keypoints)

                    eye1 = cv2.drawKeypoints(eyes[0], self.keypoints[0], eyes[0], (0, 0, 255),
                                             cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                    eye2 = cv2.drawKeypoints(eyes[1], self.keypoints[1], eyes[1], (0, 0, 255),
                                             cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

                    cv2.imshow("image2", eye1)
                    cv2.imshow("image3", eye2)
                    cv2.imshow("threshold1",img[0])
                    cv2.imshow("threshold2",img[1])



                except Exception as e:
                    # print(e)
                    pass


                try:


                    cv2.imshow("Face",face)



                except:
                    # pass
                    # print("NO FACE FOUND")
                    pass
            # Display the resulting frame


            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows()


# testing code:

if __name__ == '__main__':
    video = Video()
    video.mainloop()
