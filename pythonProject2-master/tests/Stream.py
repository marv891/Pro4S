import neoapi
import numpy as np
from PIL import Image, ImageQt
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage

camera = neoapi.Cam()
class Stream():
    ImageUpdate = pyqtSignal(QImage)

    def run(self):
        self.ThreadActive = True

        cnt = 0
        while self.ThreadActive:
            Capture = camera.GetImage()

            cnt = cnt + 1
            img = Capture.GetNPArray()

            # if img.ndim<3:
            img2 = np.append(img, img, axis=2)
            img = np.append(img2, img, axis=2)

            img = Image.fromarray(img, mode='RGB')
            qt_img = ImageQt.ImageQt(img)
            self.ImageUpdate.emit(qt_img)
            return qt_img
