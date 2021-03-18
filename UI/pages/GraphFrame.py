import tkinter as tk
from BrainWaveReader.pywave import pyWave
import matplotlib
# matplotlib backend
# random for testing sans EEG
# import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
# for live feed
import matplotlib.animation as animation
from matplotlib import style
matplotlib.use("TkAgg")
# import random
style.use("ggplot")



class GraphFrame(tk.Frame):

    def animate(self, i):
        # for test case
        # pull_data = random.randint(0, 50)

        pull_data = self.pywave.readData(self.client)
        self.dataList.append(pull_data)

        if len(self.dataList) > 20:
            y_list = self.dataList[len(self.dataList) - 20:len(self.dataList)]
        else:
            y_list = self.dataList
        self.axis.clear()
        self.axis.plot(y_list)

    def __init__(self, parent, controller):
        self.pywave = pyWave("localhost", 13854)
        self.client = self.pywave.connect()
        self.figure = Figure(figsize=(5, 5), dpi=100)
        self.axis = self.figure.add_subplot(111)

        self.dataList = []

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Frame", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        canvas = FigureCanvasTkAgg(self.figure, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def start_animation(self):
        return animation.FuncAnimation(self.figure, self.animate, interval=1000)
