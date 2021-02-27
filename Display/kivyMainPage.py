
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from Display.camera import Camera
import cv2

class MainPage(GridLayout):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        self.cols = 2 # add 2 columns
        self.lbl = Label(text="I'm with stupid -->") # create label
        self.add_widget(self.lbl) #

        self.cap = cv2.VideoCapture(0)
        self.my_camera = Camera(_capture=self.cap, _fps=30)

        self.add_widget(self.my_camera)
