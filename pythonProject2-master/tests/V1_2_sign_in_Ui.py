# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\louis\Qtdesigner_Projects\sign_in_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 256)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 70, 71, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 211, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 131, 51))
        self.label_3.setObjectName("label_3")
        self.email = QtWidgets.QLineEdit(Dialog)
        self.email.setGeometry(QtCore.QRect(150, 80, 231, 31))
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(150, 150, 231, 31))
        self.password.setObjectName("password")
        self.loginbutton = QtWidgets.QPushButton(Dialog)
        self.loginbutton.setGeometry(QtCore.QRect(290, 210, 93, 28))
        self.loginbutton.setObjectName("loginbutton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.password.setEchoMode(QLineEdit.Password)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p><span style=\" font-size:16pt;\">Email</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Please sign in </span></p></body></html>"))
        self.label_3.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:16pt;\">Password</span></p></body></html>"))
        self.loginbutton.setText(_translate("Dialog", "login"))

        self.loginbutton.clicked.connect(self.login)


    def login(self):
        if self.email.text() == 'admin' and self.password.text() == 'admin':
            loginstate = True
            print('logdin')
        else:
            loginstate = False
            print('The email or Password are incorrect')
        return loginstate


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
