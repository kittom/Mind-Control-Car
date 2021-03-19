import tkinter as tk
from UI.pages.VideoFrame import VideoFrame
from UI.pages.GraphFrame import GraphFrame


class MainPage(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.bind("<Escape>", lambda e: self.quit())
        self.title("BLI")
        self.geometry("1200x900")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # configure the rows and columns (0 is setting te minimum size, weight is the priority)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        main_frame = MainFrame(container, self)

        anim = main_frame.gf.start_animation()
        self.mainloop()


class MainFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        vf = VideoFrame(parent, self)
        self.gf = GraphFrame(parent, self)
        vf.pack()
        self.gf.pack()

if __name__ == "__main__":
    MainPage()
