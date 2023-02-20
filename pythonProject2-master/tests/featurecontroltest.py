import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import getmethod
import traceback


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self._mutex = QMutex()
        self.i = 0
        self.flag = True
        self.VBL = QVBoxLayout()


        self.entry = QtWidgets.QSpinBox()
        self.entry.setMaximum(40000)

        self.set = QPushButton("set")
        self.set.clicked.connect(self.setexp)

        self.get = QPushButton("get")
        self.get.clicked.connect(self.getexp)

        self.error = QPushButton("error")
        self.error.clicked.connect(self.errortest)

        self.output = QtWidgets.QSpinBox()
        self.output.setMaximum(40000)

        self.VBL.addWidget(self.entry)
        self.VBL.addWidget(self.output)
        self.VBL.addWidget(self.set)
        self.VBL.addWidget(self.get)
        self.VBL.addWidget(self.error)
        self.setLayout(self.VBL)

    def setexp(self):
        try:
            getmethod.setoffset(self.entry.value()/0)
        except Exception as e:
            print(type(e))
            traceback.print_exc()
        return

    def getexp(self):
        offsetx = getmethod.getoffset()
        self.output.setValue(offsetx)

    def errortest(self):
        try:
            raise Exception()
        except Exception as e:
            print(type(e))
        return

if __name__ == '__main__':
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())

