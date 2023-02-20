from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from PyQt5.uic.properties import QtCore


class ExampleWindow(QMainWindow):
    def __init__(self, windowsize):
        super().__init__()
        self.windowsize = windowsize
        self.initUI()

    def initUI(self):
        self.setFixedSize(self.windowsize)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)

        widget = QWidget()
        self.setCentralWidget(widget)
        pixmap1 = QPixmap('/bilder/20220113_000_Anwesend_2.jpg')
        #pixmap1 = pixmap1.scaledToWidth(self.windowsize.width())
        pixmap1 = pixmap1.scaled(70, 70)
        self.image = QLabel()
        self.image.setPixmap(pixmap1)
        layout_box = QHBoxLayout(widget)
        layout_box.setContentsMargins(0, 0, 0, 0)
        layout_box.addWidget(self.image)

        pixmap2 = QPixmap('/bilder/koordinaten_system_final.png')
        #pixmap2 = pixmap2.scaled(120,120)
        self.image2 = QLabel(widget)
        self.image2.setPixmap(pixmap2)
        self.image2.setFixedSize(pixmap2.size())

        p = self.geometry().bottomRight()-self.geometry().bottomRight()-QPoint(1000, 100)
        self.image2.move(p)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screensize = app.desktop().availableGeometry().size()

    ex = ExampleWindow(screensize)
    ex.show()

sys.exit(app.exec_())