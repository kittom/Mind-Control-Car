from kivy.app import App
from Display.kivyMainPage import MainPage



class CameraApp(App):
    def build(self):
        return MainPage()

if __name__ == '__main__':
    CameraApp().run()