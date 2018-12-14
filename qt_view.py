import sys
from PySide2 import QtCore, QtGui, QtWidgets


class LCDRange(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        lcd = QtWidgets.QLCDNumber(2)
        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        slider.setRange(0, 99)
        slider.setValue(0)
        self.connect(slider, QtCore.SIGNAL("valueChanged(int)"),
                     lcd, QtCore.SLOT("display(int)"))

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(lcd)
        layout.addWidget(slider)
        self.setLayout(layout)


class QtView(QtWidgets.QWidget):
    def __init__(self, parent=None, model=None):
        QtWidgets.QWidget.__init__(self, parent)
        but_quit = QtWidgets.QPushButton("Quit")
        but_quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))
        self.connect(but_quit, QtCore.SIGNAL("clicked()"),
                     QtWidgets.qApp, QtCore.SLOT("quit()"))

        grid = QtWidgets.QGridLayout()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(but_quit)
        layout.addLayout(grid)
        self.setLayout(layout)
        for row in range(9):
            for column in range(9):
                grid.addWidget(QtWidgets.QPushButton(text="hi"), row, column)
                grid.setRowMinimumHeight(row, 100)
                grid.setColumnMinimumWidth(column, 100)

    def run(self):
        self.show()





