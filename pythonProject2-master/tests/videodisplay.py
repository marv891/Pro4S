from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from V1_4_GUI_PSI_NeoAPI_Louis import *
from tests.Stream import *


class MainWindow(QWidget):
    #factor = 1.5

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
        self.Stream.resize_image.connect(self.resize_image_Slot)

        #V1_4_GUI_PSI_NeoAPI_Louis.Ui_MainWindow
        self.Stream.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)
        self.scale = 1

    global zoom

    def on_zoom_in(self):
        self._mutex.lock()
        if self.scale>1.8:
            pass
        else:
            self.scale += 0.1
        self._mutex.unlock()

    def on_zoom_out(self):
        self._mutex.lock()
        # zoom = "-"
        self.scale -= 0.1
        # self.ImageUpdateSlot(zoom)
        self._mutex.unlock()

    def resize_image_Slot(self):
        self._mutex.lock()
        size = self.Image.size()
        NImage = self.RImage.scaled(self.scale * size)
        self.FeedLabel.setPixmap(QPixmap.fromImage(NImage))
        self._mutex.unlock()

    def ImageUpdateSlot(self, Image):
        self._mutex.lock()
        size = Image.size()
        Image = Image.scaled(self.scale * size)
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






