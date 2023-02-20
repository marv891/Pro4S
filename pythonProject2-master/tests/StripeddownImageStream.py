import sys

import neoapi
import numpy as np
from PIL import Image, ImageQt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self._mutex = QMutex()

        self.flag = True
        self.VBL = QVBoxLayout()
        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.Stream = Stream()
        self.Stream.start()

        self.Stream.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)
        self.scale = 1


    def ImageUpdateSlot(self, Image):
        self._mutex.lock()
        size = Image.size()
        Image = Image.scaled(self.scale * size)
        #Dictates on wich Qlabel the image is going to be shown
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))
        self._mutex.unlock()


class Stream(QThread):
    ImageUpdate = pyqtSignal(QImage)

    def run(self):
        self.ThreadActive = True
        camera = neoapi.Cam()
        camera.Connect()
        camera.f.ExposureTime.Set(50000)
        camera.f.Gain.Set(5)

        cnt = 0
        while self.ThreadActive:
            Capture = camera.GetImage()
            cnt = cnt + 1
            img = Capture.GetNPArray()
            img2 = np.append(img, img, axis=2)
            img3 = np.append(img2, img, axis=2)
            #img4 = Image.fromarray(img, mode='RGB')
            img4 = Image.fromarray(img3, mode='RGB')
            qt_img = ImageQt.ImageQt(img4)
            self.ImageUpdate.emit(qt_img)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())
