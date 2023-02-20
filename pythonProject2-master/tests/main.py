# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
from PyQt5.QtWidgets import QApplication
from tests.videodisplay import MainWindow
from tests.Stream import Stream

Kamera_1 = "VCXG-14C"
Kamera_2 = "VCXG-13M"




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Stream = Stream.run(Kamera_1)
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())

