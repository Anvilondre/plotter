from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QLineEdit, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np
import sys


class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)

        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        self.button_defaults = QPushButton('Use default parameters')
        self.button_defaults.clicked.connect(self.set_defaults)

        self.line_A = QLineEdit('Enter A (real number)')
        self.line_B = QLineEdit('Enter B (real number)')

        self.line_bottom = QLineEdit('Enter bottom boundary (real number from interval [0, 4*pi) less than top boundary)')
        self.line_top = QLineEdit('Enter top boundary (real number from interval (0, 4*pi] bigger than bottom boundary)')

        self.label = QLabel('Fill all the parameters')
        self.label.setFont(QtGui.QFont("Arial", 10))

        self.line_precision = QLineEdit('Enter precision (positive integer)')

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        layout.addWidget(self.button_defaults)
        layout.addWidget(self.line_A)
        layout.addWidget(self.line_B)
        layout.addWidget(self.line_top)
        layout.addWidget(self.line_bottom)
        layout.addWidget(self.line_precision)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def set_defaults(self):
        self.line_A.setText("1")
        self.line_B.setText("1")
        self.line_top.setText("12.56")
        self.line_bottom.setText("0")
        self.line_precision.setText("128")

    def plot(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_title('Cycloid')
        ax.set_ylabel('Y axis')
        ax.set_xlabel('X axis')

        try:
            a = float(self.line_A.text())
            b = float(self.line_B.text())
            min = float(self.line_bottom.text())
            max = float(self.line_top.text())
            if not 0 <= min < max <= 4 * np.pi:
                raise ValueError
            precision = int(self.line_precision.text())
        except ValueError:
            self.label.setText("IllegalValue error")
            self.label.setFont(QtGui.QFont("Arial", 12))
            self.label.setStyleSheet('color: red')
            return
        else:
            self.label.setText("Everything seems ok!")
            self.label.setFont(QtGui.QFont("Arial", 11))
            self.label.setStyleSheet('color: green')

        phi = np.linspace(min, max, precision)
        x = a * phi - b * np.sin(phi) - 5
        y = a - b * np.cos(phi) - 1
        ax.plot(x, y)
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
