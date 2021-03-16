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

        self.geometry("1200x900")
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
        self.th1 = tk.DoubleVar()
        self.th2 = tk.DoubleVar()
        self.dm1_l = tk.DoubleVar()
        self.dm1_r = tk.DoubleVar(value=100)
        self.dm2_l = tk.DoubleVar()
        self.dm2_r = tk.DoubleVar(value=100)

        tk.Frame.__init__(self, parent)
        self.grid_columnconfigure(2, minsize=175)
        self.grid_columnconfigure(3, minsize=175)
        # self.grid_rowconfigure(1, minsize=height)

        # frame

        self.frame_lbl = tk.Label(self, text="frame")
        self.frame = tk.Label(self)
        self.frame_lbl.grid(column=1, row=1)
        self.frame.grid(column=1, row=2, rowspan=10)

        # face

        self.face_lbl = tk.Label(self, text="face")
        self.face = tk.Label(self)
        self.face_lbl.grid(column=2, row=1, columnspan=2)
        self.face.grid(column=2, row=2,columnspan=2)

        #  left eye
        self.eye1_lbl = tk.Label(self, text="Left Eye")
        self.eye1 = tk.Label(self)
        self.eye1_lbl.grid(column=2, row=3)
        self.eye1.grid(column=2, row=4)

        # right eye
        self.eye2_lbl = tk.Label(self, text="Right Eye")
        self.eye2 = tk.Label(self)
        self.eye2_lbl.grid(column=3, row=3)
        self.eye2.grid(column=3, row=4)

        # left eye threshold
        self.eye1_th_lbl = tk.Label(self, text="Left Eye TH")
        self.eye1_th = tk.Label(self)
        self.eye1_th_scale = tk.Scale(self, variable=self.th1, orient="horizontal")
        self.eye1_th_lbl.grid(column=2, row=5)
        self.eye1_th.grid(column=2, row=6)
        self.eye1_th_scale.grid(column=2, row=7)


        # right eye threshold
        self.eye2_th_lbl = tk.Label(self, text="Right Eye TH")
        self.eye2_th = tk.Label(self)
        self.eye2_th_scale = tk.Scale(self, variable=self.th2, orient="horizontal")
        self.eye2_th_lbl.grid(column=3, row=5)
        self.eye2_th.grid(column=3, row=6)
        self.eye2_th_scale.grid(column=3, row=7)

        # left eye direction_manager
        self.eye1_dm_lbl = tk.Label(self, text="Left Eye DM")
        self.eye1_dm = tk.Label(self)
        self.eye1_dm_scale_l = tk.Scale(self, variable=self.dm1_l, orient="horizontal")
        self.eye1_dm_scale_r = tk.Scale(self, variable=self.dm1_r, orient="horizontal")
        self.eye1_dm_lbl.grid(column=2, row=8)
        self.eye1_dm.grid(column=2, row=9)
        self.eye1_dm_scale_l.grid(column=2, row=10)
        self.eye1_dm_scale_r.grid(column=2, row=11)

        # right eye direction manager
        self.eye2_dm_lbl = tk.Label(self, text="Right Eye DM")
        self.eye2_dm = tk.Label(self)
        self.eye2_dm_scale_l = tk.Scale(self, variable=self.dm2_l, orient="horizontal")
        self.eye2_dm_scale_r = tk.Scale(self, variable=self.dm2_r, orient="horizontal")
        self.eye2_dm_lbl.grid(column=3, row=8)
        self.eye2_dm.grid(column=3, row=9)
        self.eye2_dm_scale_l.grid(column=3, row=10)
        self.eye2_dm_scale_r.grid(column=3, row=11)

        self.update_frame()

    def update_frame(self):

        _, frame = self.cap.read()
        dt = self.logic.get_data(frame)
        cv2img = dt.get_frame()
        img = PIL.Image.fromarray(cv2img)

        # frame
        try:
            frame = ImageTk.PhotoImage(image=PIL.Image.fromarray(dt.get_frame()))
            self.frame.imgtk = frame
            self.frame.configure(image=frame)
        except AttributeError:
            pass

        # face
        try:
            face = ImageTk.PhotoImage(image=PIL.Image.fromarray(dt.get_face()))
            self.face.imtk = face
            self.face.configure(image=face)
        except AttributeError:
            pass

        # eye1
        try:
            eye1 = ImageTk.PhotoImage(image=PIL.Image.fromarray(dt.get_left_eye()))
            self.eye1.imtk = eye1
            self.eye1.configure(image=eye1)
        except AttributeError:
            pass

        # eye2
        try:
            eye2 = ImageTk.PhotoImage(image=PIL.Image.fromarray(dt.get_right_eye()))
            self.eye2.imtk = eye2
            self.eye2.configure(image=eye2)
        except AttributeError:
            pass

        # eye1_th
        try:
            eye1_th = ImageTk.PhotoImage(image=PIL.Image.fromarray(dt.get_left_eye_threshold()))
            self.eye1_th.imtk = eye1_th
            self.eye1_th.configure(image=eye1_th)
        except AttributeError:
            pass

        # eye2_th
        try:
            eye2_th = ImageTk.PhotoImage(image=PIL.Image.fromarray(dt.get_right_eye_threshold()))
            self.eye2_th.imtk = eye2_th
            self.eye2_th.configure(image=eye2_th)
        except AttributeError:
            pass

        # eye1_dm
        try:
            eye1_dm = ImageTk.PhotoImage(image=PIL.Image.fromarray(dt.get_left_eye_threshold_direction_display()))
            self.eye1_dm.imtk = eye1_dm
            self.eye1_dm.configure(image=eye1_dm)
        except AttributeError:
            pass

        # eye2_dm
        try:
            eye2_dm = ImageTk.PhotoImage(image=PIL.Image.fromarray(dt.get_right_eye_threshold_direction_display()))
            self.eye2_dm.imtk = eye2_dm
            self.eye2_dm.configure(image=eye2_dm)
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