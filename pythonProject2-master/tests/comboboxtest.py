# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\louis\comboboxtest.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import neoapi
from PyQt5 import QtCore, QtGui, QtWidgets
camera = neoapi.Cam()
camera.Connect()
#neoapi.CamBase.GetFeatureList()
list = camera.GetFeatureList()
class Ui_MainWindow(object):



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(392, 147)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 30, 211, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.checkbox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_2.setObjectName("checkBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Choose Feature"))
        for f in list:
            self.comboBox.addItem(f.GetName())
        #self.comboBox.setDisabled(True)
        self.checkbox_2.stateChanged.connect(self.autotest)

    def autotest(self):
        neoapi.CExposureAuto.Get()

        #mode = neoapi.CExposureMode.value
        #print(mode)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
