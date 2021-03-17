import tkinter as tk
from UI.pages.VideoFrame import VideoFrame
import matplotlib
# matplotlib backend
matplotlib.use("TkAgg")


from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

# for live feed
import matplotlib.animation as animation
from matplotlib import style
import random









style.use("ggplot")

# inherit tkinter functionality


class UI(tk.Tk):

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
        # VideoFrame,
        for F in (StartPage, MainPage,  GraphFrame):

            frame = F(container, self)

            self.frames[F] = frame

            # sticky is the alignment and stretch (nsew is north, south, east, west)

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(GraphFrame)
        anim = animation.FuncAnimation(f, animate, interval=1000)
        self.mainloop()

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="start page", font="LARGE_FONT")
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="visit page1", command=lambda: controller.show_frame(MainPage))
        button1.pack()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # videoframe = VideoFrame(parent, controller)
        # graph_frame = GraphFrame()
        label = tk.Label(self, text="Main page", font="LARGE_FONT")
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="back to home", command=lambda: controller.show_frame(StartPage))
        button1.pack()


f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

dataList = []


def animate(i):
    global dataList
    pull_data = random.randint(0, 50)
    dataList.append(pull_data)
    if len(dataList) > 20:
        y_list = dataList[len(dataList)-20:len(dataList)]
    else:
        y_list = dataList
    a.clear()
    a.plot(y_list)


class GraphFrame(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Frame", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)





if __name__ == "__main__":
    app = UI()
