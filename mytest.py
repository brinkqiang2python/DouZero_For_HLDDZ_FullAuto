
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

plt.ion()


class AnimatedScatter(object):
    def __init__(self, numpoints=5):
        self.numpoints = numpoints

        self.x_data = ["D", "X", "2", "A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3"]
        self.y_data = [1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

        self.fig = plt.figure()
        self.fig.canvas.mpl_connect('draw_event',self.forceUpdate)
        self.ax = self.fig.add_subplot()
        
        self.ax.set_ylim([0, 4])

        self.ax.bar(self.x_data, self.y_data)

        self.ani = animation.FuncAnimation(self.fig, self.update, interval=1000, 
                                       init_func=self.setup_plot)

    def change_angle(self):
        self.y_data[0] = (self.y_data[0] - 1) % 4

    def forceUpdate(self, event):
        return

    def setup_plot(self):
        return self.ax

    def update(self, i):
        self.ax.clear()

        self.ax.bar(self.x_data, self.y_data)
        return self.ax,


    def show(self):
        plt.show()

plt.ioff()

a = AnimatedScatter()
a.show()

