# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 11:54:36 2022

@author: marvin
"""

import traceback
import CameraControl
import datetime
import time
import bver_algorithm as Off
from Layout_signIn import Ui_Dialog
from PyQt5 import QtWidgets
from inspect import currentframe, getframeinfo

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from Layout_camError import Error_Ui_Dialog
from Layout_nameFileParamter import nameParameterFileUiDialog

from Layout_LoadingParametersScreen_Button import Ui_Dialog_Loading

cnt = 0
averageCnt = 0
cam = CameraControl.camera

class GUI_functions():

    def __init__(self):
       self.scale = 1   
       self.lastFrame = 1
       self.retryCnt = 0
       
       self.Timer = QTimer()
       self.Timer.setInterval(1)
       self.Timer.timeout.connect(self.update)
       self.Timer.start()
        
       self.Timer2 = QTimer()
       self.Timer2.setInterval(1000)
       self.Timer2.timeout.connect(self.rasptime)
       self.Timer2.start()
       
    def getActualTime(self):
        """
        Retrieves the current date and time of the operating system.
        Returns
        -------
        rightdatetime : TYPE
            DESCRIPTION.

        """
        try:
            frameinfo = getframeinfo(currentframe())
            now = datetime.datetime.now()
            rightdatetime = now.strftime("%d.%m.%Y; %H:%M:%S; ")
            return rightdatetime
        except:
            self.ErrorOut.setText("Error: Failed to load current date and time. Backend, function in line: " + str(frameinfo.lineno))
    
    def update(self):
         """
         Allows to generate the Streams of frames and to display them on the aproppriate
         Qlabel in the interface.
         Every 5 frames the watchdog will signal a flashing light
         :return: Frame for Qlabel
         """
         try:
             frameinfo = getframeinfo(currentframe())
             start_time = time.time()
             global cnt
             global averageCnt
             cnt = cnt + 1
             # Frame = CameraControl.getimageMono()
             Frame = CameraControl.getimageBGR()

             # Region of interest             
             Img = Frame.scaled(self.VideoStream.size() * self.scale)
             h = int(self.verticalScrollBar.value())
             w = int(self.horizontalScrollBar.value())
             moved = Img.copy(w, h, 750, 600)                         #Muss gleich sein wie die Werte in Layout.py in Zeile 61 und 62
             
             self.verticalScrollBar.setMaximum(abs(Img.height()-Img.height()*self.scale)/2)
             self.horizontalScrollBar.setMaximum(abs(Img.width()-Img.width()*self.scale)/2)
             self.verticalScrollBar.setPageStep(self.VideoStream.height()/self.scale)
             self.horizontalScrollBar.setPageStep(self.VideoStream.width()/self.scale)
             self.VideoStream.setPixmap(QPixmap.fromImage(moved))
             
             self.retryCnt = 0
             
             if cnt > 9999:
                 cnt = 0
             if cnt % 50 == 0: # Watchdogfrequenz
                 self.flashing()
                             
             fps = 1/(time.time()-start_time)
             
             averageCnt = averageCnt + fps
             
             # Calculating fps
             if (cnt % 100) == 0:
                 averageCnt = averageCnt/100
                 self.Framenumbers.setText(str(int(round(averageCnt,0))))    
                 self.lastFrame = averageCnt
                 averageCnt = 0
            # Disabling camera pictures
             if self.lastFrame < 1: # Value has to be changed in error-message!
                 self.VideoStream.setEnabled(False)
                 self.ErrorOut.setText(self.getActualTime() + "Error: Fps value is under 1 (Fps too low).")
             else:
                 self.VideoStream.setEnabled(True)
            
         except Exception as e:  
            print(type(e))
            traceback.print_exc()
            self.retryCnt = self.retryCnt + 1
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Camera disconnected. First: Check connection to camera. Second: Restart program/timer. Backend, function in line: " + str(frameinfo.lineno))
            if self.retryCnt >= 5:
                self.windowError = QtWidgets.QDialog()
                self.uiE = Error_Ui_Dialog()
                self.uiE.setupErrorUi(self.windowError)
                self.windowError.show() 
                self.Timer.stop()
                cam.Disconnect()
                
                self.uiE.Hint1.setVisible(True)
                self.uiE.Hint2.setVisible(True)
                self.uiE.Hint3.setVisible(True)
                
                self.uiE.Retrybutton.clicked.connect(self.retryErrorUiClicked)
                
            else:
                print("hello2")
                self.windowError = QtWidgets.QDialog()
                self.uiE = Error_Ui_Dialog()
                self.uiE.setupErrorUi(self.windowError)
                self.windowError.show() 
                self.Timer.stop()
                cam.Disconnect()
                
                self.uiE.Hint1.setVisible(False)
                self.uiE.Hint2.setVisible(False)
                self.uiE.Hint3.setVisible(False)
                
                self.uiE.Retrybutton.clicked.connect(self.retryErrorUiClicked)
    
    def retryErrorUiClicked(self):
        try:
            frameinfo = getframeinfo(currentframe())
            self.windowError.close()
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to close warning window. Close all windows and restart program. Backend, function in line: " + str(frameinfo.lineno))
        try:
            cam.Connect()
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to connect to camera. Close all windows and restart program. Backend, function in line: " + str(frameinfo.lineno))
        try:
            self.Timer.start()
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to restart Timer. Close all windows and restart program. Backend, function in line: " + str(frameinfo.lineno))
    
    def manualchange(self):
        try:
            frameinfo = getframeinfo(currentframe())
            if self.Manual.isChecked():
                self.Auto.setChecked(False)
            elif not self.Manual.isChecked():
                self.Auto.setChecked(True)
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to change manual. Try again. Backend, function in line: " + str(frameinfo.lineno))
            
    def autoexptime(self):
        try:
            frameinfo = getframeinfo(currentframe())
            if self.Auto.isChecked():
                CameraControl.AutoExpTime(True)
                self.Manual.setChecked(False)
                self.Exposure_Time.setDisabled(True)
                self.Exposure_Box.setDisabled(True)
                self.TargetBrightnessbox.setDisabled(False)
                self.TargetBrightnessslider.setDisabled(False)
                self.Exposure_Box.setValue(CameraControl.getval("ExposureTime"))
                self.Exposure_Time.setValue(CameraControl.getval("ExposureTime"))
        
            elif not self.Auto.isChecked():
                CameraControl.AutoExpTime(False)
                self.Manual.setChecked(True)
                self.Exposure_Time.setDisabled(False)
                self.Exposure_Box.setDisabled(False)
                self.TargetBrightnessbox.setDisabled(True)
                self.TargetBrightnessslider.setDisabled(True)
                self.Exposure_Box.setValue(CameraControl.getval("ExposureTime"))
                self.Exposure_Time.setValue(CameraControl.getval("ExposureTime"))
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to set exposure time parameters for automatic mode. Backend, function in line: " + str(frameinfo.lineno))
    
    def setexptime(self):
        frameinfo = getframeinfo(currentframe())
        if not self.Auto.isChecked():
            try:
                CameraControl.SetExpTime(self.Exposure_Time.value())
                print(CameraControl.GetExptime())
            except Exception as e:
                print(type(e))
                traceback.print_exc()
                self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to set exposure time in manual mode. Backend, function in line: " + str(frameinfo.lineno))
            return
    
    def getexptime(self):
        try:
            frameinfo = getframeinfo(currentframe())
            exptime = CameraControl.GetExptime()
            self.Gain.setValue(exptime)
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to get exposure time and to set gain value. Backend, function in line: " + str(frameinfo.lineno))
        
    def autogain(self):
        try:
            frameinfo = getframeinfo(currentframe())
            if self.Auto.isChecked():
                CameraControl.AutoGain(True)
                self.Gain.setDisabled(True)
                self.Gain_Box.setDisabled(True)
                self.Gain_Box.setValue(CameraControl.getval("Gain"))
                self.Gain.setValue(CameraControl.getval("Gain"))
    
            elif not self.Auto.isChecked():
                CameraControl.AutoGain(False)
                self.Gain.setDisabled(False)
                self.Gain_Box.setDisabled(False)
                self.Gain_Box.setValue(CameraControl.getval("Gain"))
                self.Gain.setValue(CameraControl.getval("Gain"))
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to set gain parameters for automatic mode. Backend, function in line: " + str(frameinfo.lineno))

    def setgain(self):
        frameinfo = getframeinfo(currentframe())
        if not self.Auto.isChecked():
            try:
                CameraControl.SetGain(self.Gain.value())
                print(CameraControl.GetGain())
            except Exception as e:
                print(type(e))
                traceback.print_exc()
                self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to set gain parameters in manual mode. Backend, function in line: " + str(frameinfo.lineno))
            return

    def getgain(self):
        try:
            frameinfo = getframeinfo(currentframe())
            gain = CameraControl.GetGain()
            self.Gain.setValue(gain)
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to get gain value. Backend, function in line: " + str(frameinfo.lineno))
        
    def setbrightness(self):
        frameinfo = getframeinfo(currentframe())
        if self.Auto.isChecked():
            try:
                CameraControl.SetBrightness(self.TargetBrightnessslider.value())
                print(CameraControl.getval("TargetBrightness"))
            except Exception as e:
                print(type(e))
                traceback.print_exc()
                self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to set brightness value. Backend, function in line: " + str(frameinfo.lineno))
            return
    
    def flashing(self):
        frameinfo = getframeinfo(currentframe())
        try:
            if self.flag:
                self.Frames.setStyleSheet('background-color: none; font-size: 15px')
            else:
                self.Frames.setStyleSheet('background-color: green; font-size: 15px')
            self.flag = not self.flag
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Flashing 'Frames/s' failed. Backend, function in line: " + str(frameinfo.lineno))

    def Captureimage(self):
        try:
            frameinfo = getframeinfo(currentframe())
            CameraControl.save()
        except Exception as e:
            print(type(e))
            traceback.print_exc()
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to save image. Backend, function in line: " + str(frameinfo.lineno))
        return
    
    def openimage(self):
        try:
            frameinfo = getframeinfo(currentframe())
            CameraControl.OpenImage()
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to open image. Backend, function in line: " + str(frameinfo.lineno))
    
    def openParameterDialog(self):
        try:
            frameinfo = getframeinfo(currentframe())
            option = QFileDialog.Options()
            # first param is QWidget
            # second param is Window Title
            # third title is Default File Name
            # fourth param is FileType
            # fifth is options
    
            # for override native save dialog
            # option|=QFileDialog.DontUseNativeDialog
            file = QFileDialog.getOpenFileName(None, "Load custom parameters", "Default File", "All Files(*)", options=option)
            opendialogpath = file[0]
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to open file explorer or/and to get filepath. Backend, function in line: " + str(frameinfo.lineno))
        # Set Parameters of camera
        try:
            frameinfo = getframeinfo(currentframe())
            
            CameraControl.readSettingsOutOfFile(opendialogpath)
            
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to load custom parameters. Backend, function in line: " + str(frameinfo.lineno))
        
        try:
            frameinfo = getframeinfo(currentframe())
            # Setting the right values into the interface by checking the camera
            self.Exposure_Box.setValue(CameraControl.getval("ExposureTime"))
            self.Exposure_Time.setValue(CameraControl.getval("ExposureTime"))
            self.Gain_Box.setValue(CameraControl.getval("Gain"))
            self.Gain.setValue(CameraControl.getval("Gain"))
            self.TargetBrightnessbox.setValue(CameraControl.getval("TargetBrightness"))
            self.TargetBrightnessslider.setValue(CameraControl.getval("TargetBrightness"))
            self.loginstate = False
    
            if CameraControl.getval("ExposureTimeAuto"):
                self.Auto.setChecked(True)
                self.Manual.setChecked(False)
                self.autoexptime()
                self.autogain()
                self.TargetBrightnessbox.setDisabled(False)
                self.TargetBrightnessslider.setDisabled(False)

            else:
                self.Auto.setChecked(False)
                self.Manual.setChecked(True)
                self.autoexptime()
                self.autogain()
                self.TargetBrightnessbox.setDisabled(True)
                self.TargetBrightnessslider.setDisabled(True)
    
            self.TAxisReadOut.setDisabled(True)
            self.UAxisReadOut.setDisabled(True)
    
            if not self.loginstate:
                self.FeatureBox.setDisabled(True)
                self.LogOut.setDisabled(True)
                self.BoolBox.setDisabled(True)
                self.IntSpinBox.setDisabled(True)
                self.IntSlider.setDisabled(True)
                self.EnumBox.setDisabled(True)
                self.StringBox.setDisabled(True)
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to set GUI-parameters. Backend, function in line: " + str(frameinfo.lineno))
        return (0)
    
    def saveCustomParametersInFile(self):
        try:
            frameinfo = getframeinfo(currentframe())
            self.windowNameParameterFile = QtWidgets.QDialog()
            self.uiNPF = nameParameterFileUiDialog()
            self.uiNPF.setupNameParameterFileUi(self.windowNameParameterFile)
            self.windowNameParameterFile.show() 
            self.uiNPF.SaveButton_savingParam.clicked.connect(self.clickedSaveButton)
            self.uiNPF.CancelButton_savingParam.clicked.connect(self.clickedCancelButton)
            #     self.windowNameParameterFile.close()
            # CameraControl.saveSettingsInFile(textboxValue)
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to open filename-ui. Backend, function in line: " + str(frameinfo.lineno))
        
    def clickedCancelButton(self):
        """
        in addition to saveCustomParametersInFile
        """
        self.uiNPF.textEdit_savingParam.clear()
        self.windowNameParameterFile.close()

        
    def clickedSaveButton(self):
        """
        in addition to saveCustomParametersInFile
        """
        try:  
            frameinfo = getframeinfo(currentframe())
            textboxValue = self.uiNPF.textEdit_savingParam.toPlainText()
            self.uiNPF.textEdit_savingParam.clear()
            self.windowNameParameterFile.close()
            CameraControl.saveSettingsInFile(textboxValue)
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to save custom parameters. Backend, function in line: " + str(frameinfo.lineno))
        
    def readDefaultParametersOutOfFile(self):
        #
        try:
            frameinfo = getframeinfo(currentframe())
            CameraControl.parainit()
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to initialise default parameters. Check if 'Default' file exists. Backend, function in line: " + str(frameinfo.lineno))
        try:
            frameinfo = getframeinfo(currentframe())
            # Setting the right values into the interface by checking the camera
            self.Exposure_Box.setValue(CameraControl.getval("ExposureTime"))
            self.Exposure_Time.setValue(CameraControl.getval("ExposureTime"))
            self.Gain_Box.setValue(CameraControl.getval("Gain"))
            self.Gain.setValue(CameraControl.getval("Gain"))
            self.TargetBrightnessbox.setValue(CameraControl.getval("TargetBrightness"))
            self.TargetBrightnessslider.setValue(CameraControl.getval("TargetBrightness"))
            self.loginstate = False
    
            if CameraControl.getval("ExposureTimeAuto"):
                self.Auto.setChecked(True)
                self.Manual.setChecked(False)
                self.autoexptime()
                self.autogain()
                self.TargetBrightnessbox.setDisabled(False)
                self.TargetBrightnessslider.setDisabled(False)
            
            else:
                self.Auto.setChecked(False)
                self.Manual.setChecked(True)
                self.autoexptime()
                self.autogain()
                self.TargetBrightnessbox.setDisabled(True)
                self.TargetBrightnessslider.setDisabled(True)
    
            self.TAxisReadOut.setDisabled(True)
            self.UAxisReadOut.setDisabled(True)
    
            if not self.loginstate:
                self.FeatureBox.setDisabled(True)
                self.LogOut.setDisabled(True)
                self.BoolBox.setDisabled(True)
                self.IntSpinBox.setDisabled(True)
                self.IntSlider.setDisabled(True)
                self.EnumBox.setDisabled(True)
                self.StringBox.setDisabled(True)
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to set GUI-parameters. Backend, function in line: " + str(frameinfo.lineno))
    
    def rasptime(self):
        try:
            frameinfo = getframeinfo(currentframe())
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time)
            self.Timedisplay.setText(current_time)
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to set get and/or set time. Backend, function in line: " + str(frameinfo.lineno))
            
    def readoffset(self):
            try:
                frameinfo = getframeinfo(currentframe())
                self.Timer.stop()
                Off.measPoints = []
                dist = Off.offsetread()
                self.Timer.start()
                # if not dist == []:
                self.TAxisReadOut.setPlainText(str(dist[0]))
                self.UAxisReadOut.setPlainText(str(dist[1]))
            except Exception as e:
                print(type(e))
                traceback.print_exc()
                self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to read offset. Backend, function in line: " + str(frameinfo.lineno))
            
    def autoguigenerate(self):
        try:
            frameinfo = getframeinfo(currentframe())
            feature = self.FeatureBox.currentText()
            self.GuruFeatureName.setText(feature)
            featureval, featureinter, featuremax, featuremin, featureenumlist = CameraControl.autogenerategui(feature)
            featuredesc = CameraControl.featuredescrpition(feature)
            self.DescriptionGuru.setText(featuredesc)
    
            if featureinter == "Not Available":
                self.BoolBox.setDisabled(True)
                self.IntSpinBox.setDisabled(True)
                self.IntSlider.setDisabled(True)
                self.EnumBox.setDisabled(True)
                self.StringBox.setDisabled(True)
                self.StringBox.setPlainText(featureval)
    
            if featureinter == "bool":
                self.BoolBox.setDisabled(False)
                self.IntSpinBox.setDisabled(True)
                self.IntSlider.setDisabled(True)
                self.EnumBox.setDisabled(True)
                self.StringBox.setDisabled(True)
                self.BoolBox.setChecked(featureval)
    
            elif featureinter == "int":
                self.BoolBox.setDisabled(True)
                self.IntSpinBox.setDisabled(False)
                self.IntSlider.setDisabled(False)
                self.EnumBox.setDisabled(True)
                self.StringBox.setDisabled(True)
                if featuremax > 2147483647:
                    featuremax = featuremax / 2
                    featuremin = featuremax * -1
                self.IntSpinBox.setMaximum(int(featuremax))
                self.IntSpinBox.setMinimum(int(featuremin))
                self.IntSlider.setMaximum(int(featuremax))
                self.IntSlider.setMinimum(int(featuremin))
                self.IntSpinBox.setValue(int(featureval))
    
            elif featureinter == "float":
                self.BoolBox.setDisabled(True)
                self.IntSpinBox.setDisabled(False)
                self.IntSlider.setDisabled(False)
                self.EnumBox.setDisabled(True)
                self.StringBox.setDisabled(True)
                self.IntSpinBox.setMaximum(int(featuremax))
                self.IntSpinBox.setMinimum(int(featuremin))
                self.IntSlider.setMaximum(int(featuremax))
                self.IntSlider.setMinimum(int(featuremin))
                self.IntSpinBox.setValue(int(featureval))
    
            elif featureinter == "string":
                self.BoolBox.setDisabled(True)
                self.IntSpinBox.setDisabled(True)
                self.IntSlider.setDisabled(True)
                self.EnumBox.setDisabled(True)
                self.StringBox.setDisabled(False)
                self.StringBox.setPlainText(featureval)
    
            elif featureinter == "enum":
                self.EnumBox.clear()
                self.BoolBox.setDisabled(True)
                self.IntSpinBox.setDisabled(True)
                self.IntSlider.setDisabled(True)
                self.EnumBox.setDisabled(False)
                self.StringBox.setDisabled(True)
                self.EnumBox.addItem(featureval)
                for f in featureenumlist:
                    if not f == featureval:
                        self.EnumBox.addItem(f)
    
        except Exception as e:
            print(type(e))
            traceback.print_exc()
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to set up GUI-parameters. Backend, function in line: " + str(frameinfo.lineno))

    def featureenumset(self):
        try:
            frameinfo = getframeinfo(currentframe())
            if not self.EnumBox.currentText() is None:
                enum = self.EnumBox.currentText()
                name = self.FeatureBox.currentText()
                CameraControl.enumsetter(name, enum)
        except Exception as e:
            print(type(e))
            traceback.print_exc()
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to set enum-feature. Backend, function in line: " + str(frameinfo.lineno))
    
    def featureboolset(self):
        try:
            frameinfo = getframeinfo(currentframe())
            name = self.FeatureBox.currentText()
            if self.BoolBox.checkState():
                state = "Continuous"
            elif not self.BoolBox.checkState():
                state = "Off"
            CameraControl.boolset(name, state)
        except Exception as e:
            print(type(e))
            traceback.print_exc()
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to set bool-feature. Backend, function in line: " + str(frameinfo.lineno))
    
    def featurefloatset(self):
        try:
            frameinfo = getframeinfo(currentframe())
            name = self.FeatureBox.currentText()
            val = self.IntSpinBox.value()
            CameraControl.floatset(name, val)
        except Exception as e:
            print(type(e))
            traceback.print_exc()
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to set float-feature. Backend, function in line: " + str(frameinfo.lineno))
    
    def Description(self, featurename):
        try:
            frameinfo = getframeinfo(currentframe())
            desc = CameraControl.featuredescrpition(featurename)
            self.DescriptionStandard.setText(desc)
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to get description of feature. Description may not be available. Backend, function in line: " + str(frameinfo.lineno))
    
    def openlog(self):
        try:
            frameinfo = getframeinfo(currentframe())
            
            self.window = QtWidgets.QDialog()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self.window)
            self.window.show()
            self.ui.loginbutton.clicked.connect(self.signedin)
            
            # self.loadingScreen = QtWidgets.QDialog()
            # self.ui = Ui_Dialog_Loading()
            # self.ui.setupUi(self.loadingScreen)
            # self.loadingScreen.show()
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to open login window. Backend, function in line: " + str(frameinfo.lineno))
    
    def signedin(self):
        if self.ui.email.text() == 'admin' and self.ui.password.text() == 'admin':
            self.ui.endmessage.setText('Successfull login')
            print('logdin')
            self.FeatureBox.setDisabled(False)
            self.LogOut.setDisabled(False)
            self.BoolBox.setDisabled(False)
            self.IntSpinBox.setDisabled(False)
            self.IntSlider.setDisabled(False)
            self.EnumBox.setDisabled(False)
            self.StringBox.setDisabled(False)
            self.SignInButton.setDisabled(True)
            self.window.close()
        else:
            print('The email or Password are incorrect')
            self.ui.endmessage.setText('The Email or Password are incorrect. Please try again')
    
    def signedout(self):
        try:
            frameinfo = getframeinfo(currentframe())
            self.SignInButton.setDisabled(False)
            self.FeatureBox.setDisabled(True)
            self.LogOut.setDisabled(True)
            self.BoolBox.setDisabled(True)
            self.IntSpinBox.setDisabled(True)
            self.IntSlider.setDisabled(True)
            self.EnumBox.setDisabled(True)
            self.StringBox.setDisabled(True)
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to set up GUI-parameters. Backend, function in line: " + str(frameinfo.lineno))
    
    def coordinates(self):
        try:
            frameinfo = getframeinfo(currentframe())
            if self.Coordinates.isChecked():
                self.opacity_effect.setOpacity(1.0)
                self.CoordinatesDisplay.setGraphicsEffect(self.opacity_effect)
        
            elif not self.Coordinates.isChecked():
                self.opacity_effect.setOpacity(0.0)
                self.CoordinatesDisplay.setGraphicsEffect(self.opacity_effect)
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Coordinates-function failed. Backend, function in line: " + str(frameinfo.lineno))
            
    def zoom_in(self):
        try:
            frameinfo = getframeinfo(currentframe())
            if self.scale < 2:
                self.scale += 0.1
            self.zoomSlider.setValue(self.scale*10)
            self.update()
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to zoom in. Backend, function in line: " + str(frameinfo.lineno))
            
    def zoom_out(self):
        try:
            frameinfo = getframeinfo(currentframe())
            if self.scale > 1:
                self.scale -= 0.1         
            self.zoomSlider.setValue(self.scale*10)
            self.update()
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to zoom out. Backend, function in line: " + str(frameinfo.lineno))
            
    def zoom_slide(self):
        try:
            frameinfo = getframeinfo(currentframe())      
            self.scale = self.zoomSlider.value()/10
            self.update()
        except:
            self.ErrorOut.setText(str(self.getActualTime()) + "Error: Failed to zoom. Backend, function in line: " + str(frameinfo.lineno))