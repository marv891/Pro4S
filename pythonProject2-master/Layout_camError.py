# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\TomatoTech\Downloads\Endversionen_GUI\Layout_camError.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Error_Ui_Dialog(object):
    def setupErrorUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 250)
        Dialog.setMinimumSize(QtCore.QSize(350, 250))
        Dialog.setMaximumSize(QtCore.QSize(350, 250))
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.Hint1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Hint1.setMinimumSize(QtCore.QSize(0, 0))
        self.Hint1.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Hint1.setFont(font)
        self.Hint1.setAcceptDrops(False)
        self.Hint1.setTextFormat(QtCore.Qt.AutoText)
        self.Hint1.setAlignment(QtCore.Qt.AlignCenter)
        self.Hint1.setObjectName("Hint1")
        self.verticalLayout.addWidget(self.Hint1)
        self.Hint2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Hint2.setAlignment(QtCore.Qt.AlignCenter)
        self.Hint2.setObjectName("Hint2")
        self.verticalLayout.addWidget(self.Hint2)
        self.Hint3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Hint3.setAlignment(QtCore.Qt.AlignCenter)
        self.Hint3.setObjectName("Hint3")
        self.verticalLayout.addWidget(self.Hint3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Retrybutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Retrybutton.sizePolicy().hasHeightForWidth())
        self.Retrybutton.setSizePolicy(sizePolicy)
        self.Retrybutton.setMinimumSize(QtCore.QSize(93, 28))
        self.Retrybutton.setMaximumSize(QtCore.QSize(93, 28))
        self.Retrybutton.setAutoDefault(False)
        self.Retrybutton.setObjectName("Retrybutton")
        self.horizontalLayout.addWidget(self.Retrybutton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Camera error:"))
        self.label_2.setText(_translate("Dialog", "Camera disconnected"))
        self.Hint1.setText(_translate("Dialog", "1. Check connection to camera"))
        self.Hint2.setText(_translate("Dialog", "2. Check camera supply"))
        self.Hint3.setText(_translate("Dialog", "3. Restart program/timer"))
        self.Retrybutton.setText(_translate("Dialog", "Retry"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Error_Ui_Dialog()
    ui.setupErrorUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

