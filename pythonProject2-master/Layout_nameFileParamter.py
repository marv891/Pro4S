# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\TomatoTech\Downloads\Endversionen_GUI\Layout_nameFileParamter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class nameParameterFileUiDialog(object):
    def setupNameParameterFileUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(402, 167)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 110, 381, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.SaveButton_savingParam = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SaveButton_savingParam.setObjectName("SaveButton_savingParam")
        self.horizontalLayout_2.addWidget(self.SaveButton_savingParam)
        self.CancelButton_savingParam = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.CancelButton_savingParam.setObjectName("CancelButton_savingParam")
        self.horizontalLayout_2.addWidget(self.CancelButton_savingParam)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit_savingParam = QtWidgets.QTextEdit(Dialog)
        self.textEdit_savingParam.setGeometry(QtCore.QRect(20, 60, 371, 31))
        self.textEdit_savingParam.setObjectName("textEdit_savingParam")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SaveButton_savingParam.setText(_translate("Dialog", "Save"))
        self.CancelButton_savingParam.setText(_translate("Dialog", "Cancel"))
        self.label.setText(_translate("Dialog", "Please enter file name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = nameParameterFileUiDialog()
    ui.setupNameParameterFileUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

