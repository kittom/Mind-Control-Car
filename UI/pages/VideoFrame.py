from CarComputerVision.vidcap import EyeMotionLoop
import tkinter as tk
import PIL
from PIL import Image, ImageTk
import cv2


class VideoFrame(tk.Frame):



    def __init__(self, parent, controller):
        self.cap = cv2.VideoCapture(0)
        width, height = 800, 600
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.logic = EyeMotionLoop()
        self.th1 = tk.DoubleVar()
        self.th2 = tk.DoubleVar()
        self.dm_l = tk.DoubleVar()
        self.dm_r = tk.DoubleVar(value=100)

        tk.Frame.__init__(self, parent)
        self.grid_columnconfigure(2, minsize=175)
        self.grid_columnconfigure(3, minsize=175)
        # self.grid_rowconfigure(1, minsize=height)

        # frame

        self.frame_lbl = tk.Label(self, text="frame")
        self.frame = tk.Label(self)
        self.frame_lbl.grid(column=1, row=1)
        self.frame.grid(column=1, row=2, rowspan=11)

        # face

        self.face_lbl = tk.Label(self, text="face")
        self.face = tk.Label(self)
        self.face_lbl.grid(column=2, row=1, columnspan=2)
        self.face.grid(column=2, row=2,columnspan=2)

        #  left eye
        self.eye1_lbl = tk.Label(self, text="Left Eye")
        self.eye1 = tk.Label(self)
        self.eye1_lbl.grid(column=3, row=3)
        self.eye1.grid(column=3, row=4)

        # right eye
        self.eye2_lbl = tk.Label(self, text="Right Eye")
        self.eye2 = tk.Label(self)
        self.eye2_lbl.grid(column=2, row=3)
        self.eye2.grid(column=2, row=4)

        # left eye threshold
        self.eye1_th_lbl = tk.Label(self, text="Left Eye TH")
        self.eye1_th = tk.Label(self)
        self.eye1_th_scale = tk.Scale(self, variable=self.th1, orient="horizontal")
        self.eye1_th_lbl.grid(column=3, row=5)
        self.eye1_th.grid(column=3, row=6)
        self.eye1_th_scale.grid(column=3, row=7)


        # right eye threshold
        self.eye2_th_lbl = tk.Label(self, text="Right Eye TH")
        self.eye2_th = tk.Label(self)
        self.eye2_th_scale = tk.Scale(self, variable=self.th2, orient="horizontal")
        self.eye2_th_lbl.grid(column=2, row=5)
        self.eye2_th.grid(column=2, row=6)
        self.eye2_th_scale.grid(column=2, row=7)

        # left eye direction_manager
        self.eye1_dm_lbl = tk.Label(self, text="Left Eye DM")
        self.eye1_dm = tk.Label(self)
        self.eye1_dm_scale_l = tk.Scale(self, variable=self.dm_l, orient="horizontal")
        # self.eye1_dm_scale_r = tk.Scale(self, variable=self.dm1_r, orient="horizontal")
        self.eye1_dm_lbl.grid(column=3, row=8)
        self.eye1_dm.grid(column=3, row=9)
        self.eye1_dm_scale_l.grid(column=3, row=10)
        # self.eye1_dm_scale_r.grid(column=2, row=11)

        # right eye direction manager
        self.eye2_dm_lbl = tk.Label(self, text="Right Eye DM")
        self.eye2_dm = tk.Label(self)
        # self.eye2_dm_scale_l = tk.Scale(self, variable=self.dm2_l, orient="horizontal")
        self.eye2_dm_scale_r = tk.Scale(self, variable=self.dm_r, orient="horizontal")
        self.eye2_dm_lbl.grid(column=2, row=8)
        self.eye2_dm.grid(column=2, row=9)
        self.eye2_dm_scale_r.grid(column=2, row=10)
        # self.eye2_dm_scale_r.grid(column=3, row=11)

        # direction
        self.direction_lbl = tk.Label(self)
        self.direction_lbl.grid(column=2, row=12, columnspan=2)

        self.update_frame()

    def update_frame(self):

        _, frame = self.cap.read()

        dt = self.logic.get_data(frame, self.th1.get(), self.th2.get(), self.dm_l.get(), self.dm_r.get())
        # cv2img = dt.get_frame()


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
        try:
            direction = dt.get_direction()
            velocity = dt.get_velocity()
            self.direction_lbl.configure(text=f"Direction : {direction}, Velocity : {velocity}")
        except AttributeError:
            pass

        self.frame.after(10, self.update_frame)