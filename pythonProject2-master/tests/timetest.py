import sys
from datetime import datetime

from PyQt5.QtCore import QTimer, QMutex
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QApplication


class MainWindow(QWidget):
    #factor = 1.5

    def __init__(self):

        super(MainWindow, self).__init__()
        self._mutex = QMutex()
        self.flag = True
        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)
        self.Timer = QTimer()
        self.Timer.setInterval(1000)
        self.Timer.timeout.connect(self.time)
        self.Timer.start()


        self.setLayout(self.VBL)


    def time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        self.FeedLabel.setText(current_time)



if __name__ == '__main__':
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())
    camera = neoapi.Cam()
    camera.Connect()
    wid = QWidget()








