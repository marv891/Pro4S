# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\louis\OneDrive\Documents\systemeTechnik\2021-2022\Pro4S\Qtdesigner\GUI_V2_15.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import traceback
from PyQt5.QtCore import QMutex, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
import FeatureControle
from datetime import datetime
from tests import x_y_bverHS21_Code_WassmerSpeckert_matplotlib as Off
from V2_sign_in_Ui import Ui_Dialog


cnt = 0

class Ui_MainWindow(object):
    def __init__(self):
        self._mutex = QMutex()
        self.flag = True

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1130, 721)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.parameter_Box = QtWidgets.QTabWidget(self.centralwidget)
        self.parameter_Box.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parameter_Box.sizePolicy().hasHeightForWidth())
        self.parameter_Box.setSizePolicy(sizePolicy)
        self.parameter_Box.setMinimumSize(QtCore.QSize(319, 647))
        self.parameter_Box.setMaximumSize(QtCore.QSize(338, 563))
        self.parameter_Box.setAutoFillBackground(False)
        self.parameter_Box.setObjectName("parameter_Box")
        self.Beginner_Parameter = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Beginner_Parameter.sizePolicy().hasHeightForWidth())
        self.Beginner_Parameter.setSizePolicy(sizePolicy)
        self.Beginner_Parameter.setMinimumSize(QtCore.QSize(400, 1000))
        self.Beginner_Parameter.setMaximumSize(QtCore.QSize(1000, 1027))
        self.Beginner_Parameter.setObjectName("Beginner_Parameter")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Beginner_Parameter)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 10, 311, 525))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.StandardLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.StandardLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.StandardLayout.setContentsMargins(8, 8, 8, 8)
        self.StandardLayout.setSpacing(7)
        self.StandardLayout.setObjectName("StandardLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_6.addWidget(self.line_2)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.StandardLayout.addLayout(self.horizontalLayout_6)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.StandardLayout.addWidget(self.line)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_2.setObjectName("checkBox_2")
        self.StandardLayout.addWidget(self.checkBox_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)

        self.Exposure_Time = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.Exposure_Time.setAcceptDrops(False)
        self.Exposure_Time.setMaximum(40000)
        self.Exposure_Time.setOrientation(QtCore.Qt.Horizontal)
        self.Exposure_Time.setObjectName("Exposure_Time")
        self.horizontalLayout_3.addWidget(self.Exposure_Time)
        self.Exposure_Box = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.Exposure_Box.setMaximum(40000)
        self.Exposure_Box.setObjectName("Exposure_Box")

        self.horizontalLayout_3.addWidget(self.Exposure_Box)
        self.StandardLayout.addLayout(self.horizontalLayout_3)
        self.SetExposure = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.SetExposure.setObjectName("SetExposure")
        self.StandardLayout.addWidget(self.SetExposure)
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_3.setObjectName("checkBox_3")
        self.StandardLayout.addWidget(self.checkBox_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)

        self.Gain = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.Gain.setMaximum(250)
        self.Gain.setOrientation(QtCore.Qt.Horizontal)
        self.Gain.setObjectName("Gain")
        self.horizontalLayout_4.addWidget(self.Gain)
        self.Gain_Box = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.Gain_Box.setMaximum(250)
        self.Gain_Box.setObjectName("Gain_Box")
        self.horizontalLayout_4.addWidget(self.Gain_Box)

        self.StandardLayout.addLayout(self.horizontalLayout_4)
        self.SetGain = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.SetGain.setObjectName("SetGain")
        self.StandardLayout.addWidget(self.SetGain)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.TargetBrightness = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.TargetBrightness.setObjectName("TargetBrightness")
        self.horizontalLayout_5.addWidget(self.TargetBrightness)

        self.TargetBrightnessslider = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.TargetBrightnessslider.setMaximum(100)
        self.TargetBrightnessslider.setOrientation(QtCore.Qt.Horizontal)
        self.TargetBrightnessslider.setObjectName("TargetBrightnessslider")
        self.horizontalLayout_5.addWidget(self.TargetBrightnessslider)
        self.TargetBrightnessbox = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.TargetBrightnessbox.setMaximum(100)
        self.TargetBrightnessbox.setObjectName("TargetBrightnessbox")
        self.horizontalLayout_5.addWidget(self.TargetBrightnessbox)

        self.StandardLayout.addLayout(self.horizontalLayout_5)
        self.SetTargetBrightness = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.SetTargetBrightness.setObjectName("SetTargetBrightness")
        self.StandardLayout.addWidget(self.SetTargetBrightness)

        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox.setObjectName("checkBox")
        self.StandardLayout.addWidget(self.checkBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.StandardLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.StandardLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(160, 28))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_8.addWidget(self.plainTextEdit, 0, QtCore.Qt.AlignHCenter)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.StandardLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy)
        self.plainTextEdit_2.setMaximumSize(QtCore.QSize(160, 28))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.horizontalLayout_9.addWidget(self.plainTextEdit_2)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.StandardLayout.addLayout(self.horizontalLayout_9)
        self.Snapshot = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.Snapshot.setObjectName("Snapshot")
        self.StandardLayout.addWidget(self.Snapshot)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_loader = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.frame_loader.setObjectName("frame_loader")
        self.horizontalLayout_11.addWidget(self.frame_loader)
        self.Startbutton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.Startbutton.setObjectName("Startbutton")
        self.horizontalLayout_11.addWidget(self.Startbutton)
        self.StandardLayout.addLayout(self.horizontalLayout_11)
        self.parameter_Box.addTab(self.Beginner_Parameter, "")
        self.Parameter_BoxPage2 = QtWidgets.QWidget()
        self.Parameter_BoxPage2.setObjectName("Parameter_BoxPage2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Parameter_BoxPage2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 311, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.Gurulayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.Gurulayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.Gurulayout.setContentsMargins(8, 8, 8, 8)
        self.Gurulayout.setSpacing(7)
        self.Gurulayout.setObjectName("Gurulayout")
        self.signin = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.signin.setObjectName("signin")
        self.Gurulayout.addWidget(self.signin)
        self.FeatureList = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.FeatureList.setObjectName("FeatureList")
        self.Gurulayout.addWidget(self.FeatureList)
        self.FeatureBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.FeatureBox.setEditable(False)
        self.FeatureBox.setMaxVisibleItems(20)
        self.FeatureBox.setObjectName("FeatureBox")
        self.FeatureBox.addItem("")
        self.Gurulayout.addWidget(self.FeatureBox)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.Gurulayout.addWidget(self.pushButton)
        self.parameter_Box.addTab(self.Parameter_BoxPage2, "")
        self.gridLayout.addWidget(self.parameter_Box, 0, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(-1, -1, 8, 0)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.Zoomin = QtWidgets.QPushButton(self.centralwidget)
        self.Zoomin.setMaximumSize(QtCore.QSize(67, 16777215))
        self.Zoomin.setObjectName("Zoom in")
        self.horizontalLayout.addWidget(self.Zoomin)

        self.Zoomout = QtWidgets.QPushButton(self.centralwidget)
        self.Zoomout.setMaximumSize(QtCore.QSize(67, 16777215))
        self.Zoomout.setObjectName("Zoom out")
        self.horizontalLayout.addWidget(self.Zoomout)

        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setObjectName("time")
        self.horizontalLayout.addWidget(self.time)
        self.Timedisplay = QtWidgets.QLabel(self.centralwidget)
        self.Timedisplay.setObjectName("Timedisplay")
        self.horizontalLayout.addWidget(self.Timedisplay)

        self.Frames = QtWidgets.QLabel(self.centralwidget)
        self.Frames.setMinimumSize(QtCore.QSize(55, 16))
        self.Frames.setObjectName("Frames")
        self.horizontalLayout.addWidget(self.Frames, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.Framenumbers = QtWidgets.QLabel(self.centralwidget)
        self.Framenumbers.setMinimumSize(QtCore.QSize(50, 35))
        self.Framenumbers.setObjectName("Framenumbers")
        self.horizontalLayout.addWidget(self.Framenumbers, 0, QtCore.Qt.AlignRight)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.VideoStream = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoStream.sizePolicy().hasHeightForWidth())
        self.VideoStream.setSizePolicy(sizePolicy)
        self.VideoStream.setMinimumSize(QtCore.QSize(782, 604))
        self.VideoStream.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.VideoStream.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.VideoStream.setMouseTracking(True)
        self.VideoStream.setFrameShape(QtWidgets.QFrame.Box)
        self.VideoStream.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.VideoStream.setLineWidth(1)
        self.VideoStream.setMidLineWidth(1)
        self.VideoStream.setText("")
        # self.VideoStream.setPixmap(QtGui.QPixmap("../../../../../../../../PycharmProjects/pythonProjectGui/main/20220113_000_Anwesend_2.jpg"))
        self.VideoStream.setScaledContents(False)
        self.VideoStream.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        self.VideoStream.setObjectName("VideoStream")
        self.gridLayout.addWidget(self.VideoStream, 0, 1, 1, 1)

        self.Coordinates = QtWidgets.QLabel(self.centralwidget)
        self.Coordinates.setMinimumSize(QtCore.QSize(80, 80))
        self.Coordinates.setMaximumSize(QtCore.QSize(71, 71))
        self.Coordinates.setText("")
        self.Coordinates.setPixmap(
            QtGui.QPixmap("../../../../../../PycharmProjects/pythonProject2/koordinaten_system_final.png"))
        self.Coordinates.setScaledContents(True)
        self.Coordinates.setAlignment(QtCore.Qt.AlignCenter)
        self.Coordinates.setIndent(-1)
        self.Coordinates.setObjectName("label_3")

        self.gridLayout.addWidget(self.Coordinates, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1130, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuDevice = QtWidgets.QMenu(self.menubar)
        self.menuDevice.setObjectName("menuDevice")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuWidgets = QtWidgets.QMenu(self.menubar)
        self.menuWidgets.setObjectName("menuWidgets")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionLoad_image = QtWidgets.QAction(MainWindow)
        self.actionLoad_image.setObjectName("actionLoad_image")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionLoad_image)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDevice.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuWidgets.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        self.parameter_Box.setCurrentIndex(0)
        self.FeatureBox.setCurrentIndex(0)
        self.Exposure_Time.valueChanged['int'].connect(self.Exposure_Box.setValue)
        self.Exposure_Box.valueChanged['int'].connect(self.Exposure_Time.setValue)
        self.Gain.valueChanged['int'].connect(self.Gain_Box.setValue)
        self.Gain_Box.valueChanged['int'].connect(self.Gain.setValue)
        self.TargetBrightnessslider.valueChanged['int'].connect(self.TargetBrightnessbox.setValue)
        self.TargetBrightnessbox.valueChanged['int'].connect(self.TargetBrightnessslider.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.size()
        self.Timer = QTimer()
        self.Timer.setInterval(10)
        self.Timer.timeout.connect(self.update)
        self.Timer.start()

        self.Timer2 = QTimer()
        self.Timer2.setInterval(1000)
        self.Timer2.timeout.connect(self.rasptime)
        self.Timer2.start()

        self.scale = 1

        self.Image = None

    def retranslateUi(self, MainWindow):
        self._mutex.lock()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Feature"))
        self.label_5.setText(_translate("MainWindow", "Value"))
        self.checkBox_2.setText(_translate("MainWindow", "Auto Exposure time"))
        self.label.setText(_translate("MainWindow", "Exposure Time"))
        self.Exposure_Box.setSuffix(_translate("MainWindow", "µs"))
        self.SetExposure.setText(_translate("MainWindow", "Set Exposure time"))
        self.checkBox_3.setText(_translate("MainWindow", "Auto Gain"))
        self.label_2.setText(_translate("MainWindow", "Gain"))
        self.Gain_Box.setSuffix(_translate("MainWindow", "db"))
        self.SetGain.setText(_translate("MainWindow", "Set Gain"))
        self.TargetBrightness.setText(_translate("MainWindow", "Target Brightness"))
        self.TargetBrightnessbox.setSuffix(_translate("MainWindow", "%"))
        self.SetTargetBrightness.setText(_translate("MainWindow", "Set Target Brightness"))
        self.checkBox.setText(_translate("MainWindow", "Coordinates"))
        self.label_7.setText(_translate("MainWindow", "Preset"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Preset 1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Preset 2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Preset 180°"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Preset 0°"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Preset 90°"))
        self.label_12.setText(_translate("MainWindow", "Offset Readout"))
        self.label_8.setText(_translate("MainWindow", "T Axis"))
        self.label_9.setText(_translate("MainWindow", "mm"))
        self.label_10.setText(_translate("MainWindow", "U Axis"))
        self.label_11.setText(_translate("MainWindow", "mm"))
        self.Snapshot.setText(_translate("MainWindow", "Snapshot"))
        self.frame_loader.setText(_translate("MainWindow", "load frame"))
        self.Startbutton.setText(_translate("MainWindow", "read Offset"))
        self.parameter_Box.setTabText(self.parameter_Box.indexOf(self.Beginner_Parameter),
                                      _translate("MainWindow", "Standard"))
        self.signin.setText(_translate("MainWindow", "Sign in"))
        self.FeatureList.setText(_translate("MainWindow", "Feature List"))
        self.FeatureBox.setItemText(0, _translate("MainWindow", "Choose Feature"))
        self.pushButton.setText(_translate("MainWindow", "Feature set"))
        self.parameter_Box.setTabText(self.parameter_Box.indexOf(self.Parameter_BoxPage2),
                                      _translate("MainWindow", "Guru"))
        self.Zoomin.setText(_translate("MainWindow", "Zoom in"))
        self.Zoomout.setText(_translate("MainWindow", "Zoom out"))
        self.time.setText(_translate("MainWindow", "Time"))
        self.Timedisplay.setText(_translate("MainWindow", ""))
        self.Frames.setText(_translate("MainWindow", "Frames:"))
        self.Framenumbers.setText(_translate("MainWindow", "1"))

        self.VideoStream.setToolTip(_translate("MainWindow", "Video Frames from Camera"))
        self.VideoStream.setStatusTip(_translate("MainWindow", "Hello1"))
        self.VideoStream.setWhatsThis(_translate("MainWindow", "Hello2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuDevice.setTitle(_translate("MainWindow", "Device"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuWidgets.setTitle(_translate("MainWindow", "Widgets"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionLoad_image.setText(_translate("MainWindow", "Load image"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

        # initilise the values of parameters
        FeatureControle.parainit()
        # Setting the right values into the interface by checking the camera
        self.Exposure_Box.setValue(FeatureControle.getval("ExposureTime"))
        self.Exposure_Time.setValue(FeatureControle.getval("ExposureTime"))
        self.Gain_Box.setValue(FeatureControle.getval("Gain"))
        self.Gain.setValue(FeatureControle.getval("Gain"))
        self.TargetBrightnessbox.setValue(FeatureControle.getval("TargetBrightness"))
        self.TargetBrightnessslider.setValue(FeatureControle.getval("TargetBrightness"))
        self.loginstate = False

        if FeatureControle.getval("ExposureTimeAuto"):
            self.checkBox_2.setChecked(True)
            self.autoexptime()
        else:
            self.checkBox_2.setChecked(False)
            self.autoexptime()

        if FeatureControle.getval("GainAuto"):
            self.checkBox_3.setChecked(True)
            self.autogain()
        else:
            self.checkBox_3.setChecked(False)
            self.autogain()

        self.TargetBrightnessbox.setDisabled(True)
        self.TargetBrightnessslider.setDisabled(True)
        self.TargetBrightness.setDisabled(True)
        self.SetTargetBrightness.setDisabled(True)

        if not self.loginstate:
            self.FeatureBox.setDisabled(True)

        # Control connection of widget from the interface and which functions should be executed
        self.SetExposure.clicked.connect(self.setexptime)
        self.Exposure_Time.valueChanged.connect(self.setexptime)
        self.checkBox_2.stateChanged.connect(self.autoexptime)

        self.SetGain.clicked.connect(self.setgain)
        self.Gain.valueChanged.connect(self.setgain)
        self.checkBox_3.stateChanged.connect(self.autogain)

        self.SetTargetBrightness.clicked.connect(self.setbrightness)
        self.TargetBrightnessslider.valueChanged.connect(self.setbrightness)

        self.Snapshot.clicked.connect(self.Captureimage)
        self.actionLoad_image.triggered.connect(self.openimage)

        self.Zoomin.clicked.connect(self.zoom_in)
        self.Zoomout.clicked.connect(self.zoom_out)

        self.Startbutton.clicked.connect(self.readoffset)

        self.pushButton.clicked.connect(self.autoguigenerate)

        self.signin.clicked.connect(self.openlog)

        self.featurenamelist = FeatureControle.GetMasterFeatureList()
        # self.featurenamelist = FeatureControle.GetFeatureList()
        for f in self.featurenamelist:
            self.FeatureBox.addItem(f[0])

    def update(self):
        """
Allows to generate the Streams of frames and to display them on the aproppriate
Qlabel in the interface.
Every 5 frames the watchdog will signal a flashing light
        :return: Frame for Qlabel
        """
        try:
            global cnt
            cnt = cnt + 1
            Frame = FeatureControle.getimageMono()
            # Frame = FeatureControle.getimageBGR()
            Img = Frame.scaled(self.VideoStream.size() * self.scale)
            self.VideoStream.setPixmap(QPixmap.fromImage(Img))
            self.Framenumbers.setText(str(cnt))
            if cnt > 9999:
                cnt = 0
            if cnt % 5 == 0:
                ui.flashing()
        # print(cnt)
        except Exception as e:
            print(type(e))
            traceback.print_exc()
        return Frame

    def autoexptime(self):

        if self.checkBox_2.isChecked():
            FeatureControle.AutoExpTime(True)
            self.Exposure_Time.setDisabled(True)
            self.Exposure_Box.setDisabled(True)
            self.SetExposure.setDisabled(True)
            self.TargetBrightnessbox.setDisabled(False)
            self.TargetBrightnessslider.setDisabled(False)
            self.TargetBrightness.setDisabled(False)
            self.SetTargetBrightness.setDisabled(False)
            self.Exposure_Box.setValue(FeatureControle.getval("ExposureTime"))
            self.Exposure_Time.setValue(FeatureControle.getval("ExposureTime"))

        elif not self.checkBox_2.isChecked():
            FeatureControle.AutoExpTime(False)
            self.Exposure_Time.setDisabled(False)
            self.Exposure_Box.setDisabled(False)
            self.SetExposure.setDisabled(False)
            self.TargetBrightnessbox.setDisabled(True)
            self.TargetBrightnessslider.setDisabled(True)
            self.TargetBrightness.setDisabled(True)
            self.SetTargetBrightness.setDisabled(True)
            self.Exposure_Box.setValue(FeatureControle.getval("ExposureTime"))
            self.Exposure_Time.setValue(FeatureControle.getval("ExposureTime"))

    def setexptime(self):
        if not self.checkBox_2.isChecked():
            try:
                FeatureControle.SetExpTime(self.Exposure_Time.value())
                print(FeatureControle.GetExptime())
            except Exception as e:
                print(type(e))
                traceback.print_exc()
            return

    def getexptime(self):
        exptime = FeatureControle.GetExptime()
        self.Gain.setValue(exptime)

    def autogain(self):

        if self.checkBox_3.isChecked():
            FeatureControle.AutoGain(True)
            self.Gain.setDisabled(True)
            self.Gain_Box.setDisabled(True)
            self.SetGain.setDisabled(True)
            self.Gain_Box.setValue(FeatureControle.getval("Gain"))
            self.Gain.setValue(FeatureControle.getval("Gain"))

        elif not self.checkBox_3.isChecked():
            FeatureControle.AutoGain(False)
            self.Gain.setDisabled(False)
            self.Gain_Box.setDisabled(False)
            self.SetGain.setDisabled(False)
            self.Gain_Box.setValue(FeatureControle.getval("Gain"))
            self.Gain.setValue(FeatureControle.getval("Gain"))

    def setgain(self):
        if not self.checkBox_3.isChecked():
            try:
                FeatureControle.SetGain(self.Gain.value())
                print(FeatureControle.GetGain())
            except Exception as e:
                print(type(e))
                traceback.print_exc()
            return

    def getgain(self):
        gain = FeatureControle.GetGain()
        self.Gain.setValue(gain)

    def setbrightness(self):
        if self.checkBox_2.isChecked():
            try:
                FeatureControle.SetBrightness(self.TargetBrightnessslider.value())
                print(FeatureControle.getval("TargetBrightness"))
            except Exception as e:
                print(type(e))
                traceback.print_exc()
            return

    def flashing(self):
        # self._mutex.lock()
        if self.flag:
            self.Frames.setStyleSheet('background-color: none; font-size: 15px')
        else:
            self.Frames.setStyleSheet('background-color: green; font-size: 15px')
        self.flag = not self.flag
        # self._mutex.unlock()

    def Captureimage(self):
        try:
            FeatureControle.save()
        except Exception as e:
            print(type(e))
            traceback.print_exc()
        return

    def openimage(self):
        FeatureControle.OpenImage()

    def zoom_in(self):
        if self.scale <2:
            self.scale *= 1.1
            print(self.scale)
            self.update()

    def zoom_out(self):
        self.scale /= 1.1
        print(self.scale)
        self.update()
        if self.scale < 1:
            self.scale = 1

    def rasptime(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        # print("Current Time =", current_time)
        self.Timedisplay.setText(current_time)

    def readoffset(self):
        dist = Off.offsetread()
        self.plainTextEdit.setPlainText(str(dist[0]))
        self.plainTextEdit_2.setPlainText(str(dist[1]))

    def autoguigenerate(self):
        feature = self.FeatureBox.currentText()
        featureval = FeatureControle.autogenerategui(feature)
        label = QtWidgets.QLabel()
        self.Gurulayout.addWidget(label)
        label.setText(str(featureval))

    def openlog(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.loginbutton.clicked.connect(self.signedin)

    def signedin(self):
        if self.ui.email.text() == 'admin' and self.ui.password.text() == 'admin':
            self.ui.endmessage.setText('Successfull login')
            print('logdin')
            self.FeatureBox.setDisabled(False)
            self.window.close()
        else:
            print('The email or Password are incorrect')
            self.ui.endmessage.setText('The Email or Password are incorrect. Please try again')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
