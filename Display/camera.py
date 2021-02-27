from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2

class Camera(Image):


    def __init__(self, _capture, _fps, **kwargs):
        super(Camera, self).__init__(**kwargs)
        self.cap = _capture
        Clock.schedule_interval(self.update, 1.0 / _fps)

    def update(self, dt):
        ret, frame = self.cap.read()

        if ret:
            print(ret)
            # convert it to texture
            # print(frame.shape[1])
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.texture = image_texture

