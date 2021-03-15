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
        width, height = 800, 600
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.logic = EyeMotionLoop()

        tk.Frame.__init__(self, parent)
        self.grid_columnconfigure(2, minsize=350)
        # self.grid_rowconfigure(1, minsize=height)

        self.frame_lbl = tk.Label(self, text="frame")
        self.frame = tk.Label(self)
        self.frame_lbl.grid(column=1, row=1)
        self.frame.grid(column=1, row=2, rowspan=3)

        self.face_lbl = tk.Label(self, text="face")
        self.face = tk.Label(self)
        self.face_lbl.grid(column=2, row=1, columnspan=2)
        self.face.grid(column=2, row=2,columnspan=2)

        self.eye1_lbl = tk.Label(self, text="Left Eye")
        self.eye1 = tk.Label(self)
        self.eye1_lbl.grid(column=2, row=3)
        self.eye1.grid(column=2, row=4)



        self.update_frame()

    def update_frame(self):

        _, frame = self.cap.read()
        dt = self.logic.get_data(frame)
        cv2img = dt.get_frame()
        img = PIL.Image.fromarray(cv2img)
        try:
            frame = ImageTk.PhotoImage(image=PIL.Image.fromarray(dt.get_frame()))
            self.frame.imgtk = frame
            self.frame.configure(image=frame)
        except AttributeError:
            pass

        try:
            face = ImageTk.PhotoImage(image=PIL.Image.fromarray(dt.get_face()))
            self.face.imtk = face
            self.face.configure(image=face)
        except AttributeError:
            pass

        try:
            eye1 = ImageTk.PhotoImage(image=PIL.Image.fromarray(dt.get_left_eye()))
            self.eye1.imtk = eye1
            self.eye1.configure(image=eye1)
        except AttributeError:
            pass

        self.frame.after(10, self.update_frame)



























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