from tkinter import *
from CarComputerVision.videocapture import Video

master = Tk()

if __name__ == '__main__':
    w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
    w.pack()

    video = Video()
    video.mainloop()
    mainloop()
