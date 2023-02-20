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
    factor = 1.5

    def __init__(self):
        super(MainWindow, self).__init__()
        self._mutex = QMutex()

        self.flag = True
        self.VBL = QVBoxLayout()
        # self._scene = QtWidgets.QGraphicsScene(self)
        # self._view = QtWidgets.QGraphicsView(self._scene)
        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)
        # self.Watchdog= QLabel()
        # self.VBL.addWidget(self.Watchdog)

        self.Watchdog = QPushButton("Watchdog")
        self.Watchdog.clicked.connect(self.flashing)
        self.VBL.addWidget(self.Watchdog)

        self.CancelBTN = QPushButton("Cancel")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

        self.ZoomButtonIn = QPushButton("Zoom in")
        self.ZoomButtonIn.clicked.connect(self.on_zoom_in)
        self.VBL.addWidget(self.ZoomButtonIn)

        self.ZoomButtonOut = QPushButton("Zoom out")
        self.ZoomButtonOut.clicked.connect(self.on_zoom_out)
        self.VBL.addWidget(self.ZoomButtonOut)

        self.Stream = Stream()
        self.Stream.start()
        #self.Stream.resize_image.connect(self.resize_image_Slot)

        self.Stream.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)
        self.scale = 1
        self.zoom = None

    def on_zoom_in(self):
        self._mutex.lock()
        # zoom = "+"
        self.scale *= 2
        # self.ImageUpdateSlot(zoom)
        self._mutex.unlock()

    def on_zoom_out(self):
        self._mutex.lock()
        # zoom = "-"
        self.scale /= 2
        # self.ImageUpdateSlot(zoom)
        self._mutex.unlock()

    #def resize_image_Slot(self):
        #self._mutex.lock()
        #size = self.Image.size()
        #NImage = self.RImage.scaled(self.scale * size)
        #self.FeedLabel.setPixmap(QPixmap.fromImage(NImage))
        #self._mutex.unlock()

    def ImageUpdateSlot(self, Image):
        self._mutex.lock()
        # if zoom=="+" or zoom=="-":
        size = Image.size()
        Image = Image.scaled(self.scale * size)
        # self.FeedLabel.setPixmap(QPixmap.fromImage(Image))
        # else:
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))
        self._mutex.unlock()

    def CancelFeed(self):
        self._mutex.lock()
        self.Stream.stop()
        self._mutex.unlock()

    def flashing(self):
        self._mutex.lock()

        if self.flag:
            self.Watchdog.setStyleSheet('background-color: none; font-size: 15px')
        else:
            self.Watchdog.setStyleSheet('background-color: green; font-size: 15px')

        self.flag = not self.flag
        self._mutex.unlock()


class Stream(QThread):
    ImageUpdate = pyqtSignal(QImage)

    # resize_image = pyqtSignal(QImage)

    def run(self):
        self.ThreadActive = True
        camera = neoapi.Cam()
        camera.Connect()
        camera.f.ExposureTime.Set(15000)
        camera.f.Gain.Set(1)
        #camera.f.PixelFormat.GetEnumValueList().IsReadable('Mono8')
        #camera.f.PixelFormat.SetString('Mono8')
        cnt = 0
        while self.ThreadActive:
            Capture = camera.GetImage()
            # if Capture:
            cnt = cnt + 1
            img = Capture.GetNPArray()
            # print(img.shape)
            #if img.ndim<3:
            img2 = np.append(img, img, axis=2)
            img3 = np.append(img2, img, axis=2)

            # print(img.shape)
            img4 = Image.fromarray(img3, mode='RGB')
            qt_img = ImageQt.ImageQt(img4)
            self.ImageUpdate.emit(qt_img)
            # self.resize_image.emit(qt_img)

            if cnt % 5 == 0:
                Root.flashing()

            print(cnt)

    # def stop(self):
    # self._mutex.lock()
    # self.ThreadActive = False
    # self.quit()
    # self._mutex.unlock()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())
