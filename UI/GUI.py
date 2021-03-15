from CarComputerVision.vidcap import EyeMotionLoop
import tkinter as tk
import PIL
from PIL import Image, ImageTk
import cv2

# inerit tkinter functionality
class ui(tk.Tk):

    def __init__(self, *args,**kwargs ):

        tk.Tk.__init__(self, *args, **kwargs)
        self.bind("<Escape>", lambda e: self.quit())
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # configue the rows and columns (0 is setting te minimum size, weight is the priority)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, MainPage, VideoPage):

            frame = F(container, self)

            self.frames[F] = frame

            # sticky is the alignment and stretch (nsew is north, south, east, west)

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(VideoPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="start page", font="LARGE_FONT")
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="visit page1", command=lambda : controller.show_frame(MainPage))
        button1.pack()

    @staticmethod
    def qf():
        print("button pressed")


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main page", font="LARGE_FONT")
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="back to home", command=lambda: controller.show_frame(StartPage))
        button1.pack()


class VideoPage(tk.Frame):



    def __init__(self, parent, controller):
        self.cap = cv2.VideoCapture(0)
        self.logic = EyeMotionLoop()
        tk.Frame.__init__(self, parent)
        self.lmain = tk.Label(self)
        self.lmain.pack()

        self.get_dt()


    def get_dt(self):


        # print("repeat")
        _, frame = self.cap.read()
        dt = self.logic.get_data(frame)
        cv2img = dt.get_frame()
        img = PIL.Image.fromarray(cv2img)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)

        self.lmain.after(10, self.get_dt)



























if __name__ == "__main__":
    app = ui()
    app.mainloop()










# logic = EyeMotionLoop()
#
# cap = cv2.VideoCapture(0)
#
# while True:
#
#     ret, frame = cap.read()
#
#     if ret:
#
#         dt = logic.get_data(frame)
#
#         cv2.imshow("frame", dt.get_frame())
#
#         # dt = logic.mainloop(dt)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#             # When everything done, release the capture
#
# cap.release()
# cv2.destroyAllWindows()