import datetime
import sys

import neoapi
import numpy as np
from PIL import Image, ImageQt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from V1_4_GUI_PSI_NeoAPI_Louis import *

class MainWindow(QWidget):
    #factor = 1.5

    def __init__(self):

        super(MainWindow, self).__init__()
        self._mutex = QMutex()
        self.i = 0
        self.flag = True
        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.Watchdog = QPushButton("Watchdog")
        self.Snapshot = QPushButton("Snapshot")
        self.Watchdog.clicked.connect(self.flashing)
        self.Snapshot.clicked.connect(self.opensavedialogue)
        self.VBL.addWidget(self.Watchdog)
        self.VBL.addWidget(self.Snapshot)

        self.setLayout(self.VBL)
        #self.Timer = QTimer()
        #self.Timer.setInterval(1000)
        #self.Timer.timeout.connect(self.time())
        #self.Timer.start()

    def flashing(self):
        button2 = QPushButton(str(self.i))
        self.i = self.i + 1
        self.VBL.addWidget(button2)
        number = self.VBL.count()
        if number > 5:
            self.VBL.removeWidget(self.VBL.itemAt(2).widget())

    def screenshot(self):
        Capture = camera.GetImage()
        img = Capture.GetNPArray()
        img = Image.fromarray(img, mode='RGB')
        qt_img = ImageQt.ImageQt(img)
        return qt_img

    def opensavedialogue(self):
        option = QFileDialog.Options()
        file = QFileDialog.getSaveFileName(QWidget,"Save File Window Title","defualt.txt","All Files(*)",options=option)
        print(file)




if __name__ == '__main__':
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())
    camera = neoapi.Cam()
    camera.Connect()
    wid = QWidget()

