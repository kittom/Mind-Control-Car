import tkinter as tk
# from BrainWaveReader.pywave import pyWave
import matplotlib
# matplotlib backend
# random for testing sans EEG
# import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
# for live feed
import matplotlib.animation as animation
from matplotlib import style
import random
from BrainWaveReader.FileManager import FileManager
matplotlib.use("TkAgg")

style.use("ggplot")



class GraphFrame(tk.Frame):

    def animate(self, i):
        # for test case
        pull_data = random.randint(0,100)
        # pull_data = self.pywave.readData(self.client)
        self.file_manager.add_dt(pull_data)
        self.dataList.append(pull_data)

        if len(self.dataList) > 100:
            y_list = self.dataList[len(self.dataList) - 100:len(self.dataList)]
        else:
            y_list = self.dataList
        self.axis.clear()
        self.axis.plot(y_list)


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.file_manager = FileManager()

        # self.pywave = pyWave("localhost", 13854)
        # self.client = self.pywave.connect()
        self.figure = Figure(figsize=(10, 2), dpi=100)
        self.axis = self.figure.add_subplot(111)

        self.dataList = []

        label = tk.Label(self, text="Graph Frame", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        canvas = FigureCanvasTkAgg(self.figure, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def start_animation(self):
        return animation.FuncAnimation(self.figure, self.animate, interval=1000)
