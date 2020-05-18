from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cycloid plotter!")
        self.setGeometry(600, 300, 600, 600)

        self.MyUI()

    def MyUI(self):
        canvas = Canvas(self, width=4, height=3)
        canvas.move(0, 0)

        plot_button = QPushButton("Plot!", self)
        plot_button.move(100, 450)
        plot_button.clicked.connect(canvas.plot)

        save_button = QPushButton("Save", self)
        save_button.move(250, 450)
        save_button.clicked.connect(canvas.save)


class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        fig.suptitle("Cycloid")

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.plot()

    def save(self):
        self.figure.savefig('plot.png')

    def plot(self, a=1, b=1, boundary=(4*np.pi)):
        a = get_input("A")
        b = get_input("B")
        phi = np.linspace(0, boundary, 128)
        x = a * phi - b * np.sin(phi)
        y = a - b * np.cos(phi)
        ax = self.figure.add_subplot()
        ax.plot(x, y)


def get_input(name, min=None, max=None):
    while True:
        try:
            a = float(input("Enter " + name + ": "))
            if min is not None:
                if max is not None:
                    if not min <= a <= max:
                        raise ValueError
                else:
                    if not min <= a:
                        raise ValueError
            elif max is not None:
                if not a <= max:
                    raise ValueError
            return a
        except ValueError:
            print("Oops!  That was no valid value.  Try again...")


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
# a = get_input("A")
# b = get_input("B")
# x, y = get_plot_data(a, b)
# plt.xlabel("X axis")
# plt.ylabel("Y axis")
# plt.plot(x, y)
# plt.show()
