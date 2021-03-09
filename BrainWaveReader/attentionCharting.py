import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from BrainWaveReader.pywave import pyWave


y_vals = []
pywave = pyWave("localhost", 13854)
client = pywave.connect()



def get_dt(i):

    y_vals.append(pywave.readData(client))
    # plt.axes.set
    plt.cla()
    if len(y_vals) > 100:
        # print(y_vals[len(y_vals)-100:len(y_vals)])
        plt.plot(y_vals[len(y_vals)-100:len(y_vals)])
    else:
        plt.plot(y_vals)


plt.style.use("fivethirtyeight")


animation = FuncAnimation(plt.gcf(), get_dt, interval = 500)


plt.tight_layout()
plt.show()

