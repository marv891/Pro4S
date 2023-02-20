import csv
import traceback
import neoapi
from neoapi import Feature
import numpy as np
from PIL import Image, ImageQt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QWidget
import os
import pickle

from Layout_LoadingParametersScreen_Button import Ui_Dialog_Loading
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QLabel, QApplication
from PyQt5 import QtWidgets
import time

from PyQt5.QtCore import QTimer

#*********************************************************************************************************************
# This file contains all control function for the interface, the connection with the neoApi is done
# sepratly from the main file as to limit Errors.
#*********************************************************************************************************************

camera = neoapi.Cam()
camera.Connect()
widget = QWidget


try:

    def parainit():
        """
        The Function paraint() will be called when the program is first started to define the default value the user
        will find.
        # When Using the VCXG-24c Camera it is essential to set the Binning parameter to 2. Otherwise the
        amount of data received by the program will be to high and it will crash.
        This parameter is not to be changed !!!
        The later parameters are simply set to ease the user during start up and as to not crash the
        program immediately ^^'.
        These Values have mostly been chosen based on experimentation, 10000 for the
        exposure time for not over working the process, A very high gain allows for a very low exposure time,
        hence 36 db The Binning function should always be set on 2 to ease the processing load of the raspberry,
        set on 1 ist not Recommended
        """        
        try:
            # readSettingsOutOfFile('data\Default') # Version for Windows
            readSettingsOutOfFile('data/Default') # Version for Raspberry-Pi
# =============================================================================
#             In case function above doesn´t work
# =============================================================================
#             # open a file, where pickled data is stored 
#             # file = open('data\Default', 'rb')
#             file = open('data\Default', 'rb')
#             # dump information out of file
#             listComplete = pickle.load(file)
#             # close the file
#             file.close()
#             # Read values for parameters and set features afterwards
#             for item in range(len(listComplete[0])):
#                 feature = listComplete[0][item]
#                 value = listComplete[1][item]
#                 camera.SetFeature(feature, value)
# =============================================================================
            print("Parameters are set")
            
        except Exception as e:
            print(type(e))
            traceback.print_exc()
            
            #camera.SetFeature("ExposureAuto", "Continuous")
            camera.SetFeature("ExposureAuto", "Off")
            camera.SetFeature("GainAuto", "Off")
            camera.f.BinningVertical.Set(6)                     # Do not change the value to 1 or 2 --> fps are way too low on raspberry-pi
            camera.f.BinningHorizontal.Set(6)                   # Do not change the value to 1 or 2 --> fps are way too low on raspberry-pi
            #camera.SetFeature("ExposureTime", 5000)
            camera.f.ExposureTime.Set(10000)
            camera.f.Gain.Set(36)
            camera.f.BrightnessAutoNominalValue.Set(50)
            #camera.SetFeature("BalanceWhiteAuto","Continuous")

    def getimageMono():
        """
        Allows to get a single frame from the Monochrome Baumer Camera
        In Order to process the image received from a Monochrome Camera,
        2 additional dimension need to be added to to the picture to simulate
        the structure of a colored image
        :return: object
        """
        Capture = camera.GetImage()
        img = Capture.GetNPArray()
        img2 = np.append(img, img, axis=2)
        img3 = np.append(img2, img, axis=2)
        img4 = Image.fromarray(img3, mode='RGB')
        qt_img = ImageQt.ImageQt(img4)
        return qt_img

    def getimageBGR():
        """
        Allows to get a single frame from the Baumer Camera
        :return: ImageQT type
        """
        Capture = camera.GetImage()
        img = Capture.GetNPArray()
        img2 = Image.fromarray(img, mode='RGB')
        print("Test250123")

        qt_img = ImageQt.ImageQt(img2)
        return qt_img

    def image():
        """
        Test image used during debugging
        :return:
        """
        image = '20220113_000_Anwesend_2.jpg'
        return QPixmap(image)

    def getval(Para):
        """
        :param Para: Name of the Parameter to get
        :return: The value of said parameter
        """
        if Para == "ExposureTime":
            val = camera.f.ExposureTime.Get()
            return int(val)
        elif Para == "ExposureTimeAuto":
            val = camera.GetFeature("ExposureAuto").GetString()
            if val == "Off":
                state = False
            elif val == "Continuous":
                state = True
            return state
        elif Para == "Gain":
            val = camera.f.Gain.Get()
            return int(val)
        elif Para == "GainAuto":
            val = camera.GetFeature("GainAuto").GetString()
            if val == "Off":
                state = False
            elif val == "Continuous":
                state = True
            return state
        elif Para == "TargetBrightness":
            val = camera.f.BrightnessAutoNominalValue.Get()
            return int(val)

    def AutoExpTime(stateexp):
        """
        Function called to set Automatic Exposure time Function
        :param stateexp:
        """
        if camera.HasFeature("ExposureAuto"):
            if camera.IsWritable("ExposureAuto"):
                if stateexp:
                    camera.SetFeature("ExposureAuto", "Continuous")
                # print("  ExposureAuto                   ", camera.GetFeature("ExposureAuto").GetString())
                # print(camera.HasFeature("ExposureAuto"))
                else:
                    camera.SetFeature("ExposureAuto", "Off")

    def AutoGain(stategain):
        """
        Function called to set Automatic Gain Function
        :param stategain:
        """
        if camera.HasFeature("GainAuto"):
            if camera.IsWritable("GainAuto"):
                if stategain:
                    camera.SetFeature("GainAuto", "Continuous")
                # print("  ExposureAuto                   ", camera.GetFeature("ExposureAuto").GetString())
                # print(camera.HasFeature("ExposureAuto"))
                else:
                    camera.SetFeature("GainAuto", "Off")

    def SetExpTime(valExpTim):
        """
        Function Dynamically called upon when Slider of Exposure time is moved
        Allows setting the Exposure time based on Min and Max Values of Camera
        :param valExpTim:
        :return:
        """
        if valExpTim > camera.f.ExposureTime.GetMax():
            print(f"The chosen Exposure Time exceeds current limits of {camera.f.ExposureTime.GetMax()}, Over limit")
        elif valExpTim < camera.f.ExposureTime.GetMin():
            print(f"The chosen Exposure Time exceeds current limits of {camera.f.ExposureTime.GetMin()}, Negative Value")
        else:
            camera.f.ExposureTime.Set(valExpTim)
        return

    def SetGain(valGain):
        """
        Function Dynamically called upon when Slider of Gain is moved
        Allows setting the Gain based on Min and Max Values of Camera
        :param valGain:
        :return:
        """
        if valGain > camera.f.Gain.GetMax():
            print(f"The chosen Gain exceeds current limits of {camera.f.Gain.GetMax()}, Over limit")
        elif valGain < camera.f.Gain.GetMin():
            print(f"The chosen Gain exceeds current limits of {camera.f.Gain.GetMin()}, Negative Value")
        else:
            camera.f.Gain.Set(valGain)
        return

    def SetBrightness(valbright):
        """
        This Function can Only be set when Exposure and Gain are Set in Continuous Mode
        Function Dynamically called upon when Slider of BrightnessAutoNominalValue is moved
        Allows setting the BrightnessAutoNominalValue based on Min and Max Values of Camera
        :param valbright:
        :return:
        """
        if valbright > camera.f.BrightnessAutoNominalValue.GetMax():
            print(f"The chosen Gain exceeds current limits of "
                  f"{camera.f.BrightnessAutoNominalValue.GetMax()}, Over limit")
        elif valbright < camera.f.BrightnessAutoNominalValue.GetMin():
            print(f"The chosen Gain exceeds current limits of "
                  f"{camera.f.BrightnessAutoNominalValue.GetMin()}, Negative Value")
        else:
            camera.f.BrightnessAutoNominalValue.Set(valbright)
        return

    def GetFeatureList():
        """
        Calles upon all the Features Available on the connected Camera and Stores the Names in a List
        :return:
        """
        list = []
        featurelist = camera.GetFeatureList()
        for f in featurelist:
            list.append(f.GetName())
            # print(f.GetInterface())
            # if f.GetInterface() == "ICategory":
            # print(f)
        return list

    def saveSettingsInFile(filename):
        """
        written by programmer
        """
        try:
            # Creating path of relative path to folder data
            absolutepath = os.path.abspath(__file__)  
            #Path of filedirectory
            fileDirectory = os.path.dirname(absolutepath)
            #Path of parent directory
            #parentDirectory = os.path.dirname(fileDirectory)
            #Navigate to data directory
            newPath = os.path.join(fileDirectory, 'data')
            #Creating new filepath with filename if file doesn't exists
            newFilePath = os.path.join(newPath, filename)
            #newFilePath2 = os.path.join(newFilePath, '.csv')
            print(newPath)
            
            featurelist = camera.GetFeatureList()
            
            Filename = newFilePath + '(Readable).csv'

            # Creating readable file
            file = open(Filename, "w")
            for f in featurelist:
                if f.IsReadable() and f.IsWritable():
                    file.write(f.GetName())
                    file.write(";")
                    file.write(f.GetInterface())
                    file.write(";")
                    file.write(str(f.GetValue()))
                    file.write("\n")
                else:
                    pass
            file.close()
        
            # Creating Pickle-file:
            listf = [] # List for readable and writable features
            listv = [] # List for values of features
            
            listComplete = []
            
            featurelist = camera.GetFeatureList()
            for f in featurelist:
                if f.GetName() == 'GevSCDA':
                    pass
                elif f.GetName() == 'GevSCPSPacketSize':
                    pass
                elif f.IsReadable() and f.IsWritable():
                    listf.append(f.GetName())
                    listv.append(f.GetValue())
            listComplete.append(listf)
            listComplete.append(listv)
            
            # open a file, where you want to store the data
            pickelFile = open(newFilePath, 'wb')
            # dump information to that file
            pickle.dump(listComplete, pickelFile)
            pickelFile.close()
            
        except Exception as e:
            print(type(e))
            traceback.print_exc()

        return 0
       
    def readSettingsOutOfFile(filename):
        try:    
            # Open Loading screen
            
# =============================================================================
#       PROBLEM
#             loadingScreen = QtWidgets.QDialog()
#             ui = Ui_Dialog_Loading()
#             ui.setupUi(loadingScreen)
#             loadingScreen.show()
# =============================================================================
            # itemscnt = 0
            
# =============================================================================
#             loadingScreen = QtWidgets.QDialog()
#             uiL = Ui_Dialog_Loading()
#             uiL.setupLoadingUi(loadingScreen)
#             loadingScreen.show()
# =============================================================================
            
            # Open the file, where pickled data is stored 
            file = open(filename, 'rb')
            # Dump information out of file
            listComplete = pickle.load(file)
            # Close the file
            file.close()
            
            # Read values for parameters and set features afterwards
            for item in range(len(listComplete[0])):
                feature = listComplete[0][item]
                value = listComplete[1][item]
                if feature == 'Gain':
                    pass
                elif feature == 'GevSCDA':
                    pass
                elif feature == 'GevSCPSPacketSize':
                    pass
                else:
                    print(feature)
                    camera.SetFeature(feature, value)
                # itemscnt = itemscnt + 1
                
                # setProperty("value", value)   
            
            print("Parameters are set")
          
        except Exception as e:
            print(type(e))
            traceback.print_exc()
        
    def GetMasterFeatureList():
        """
        List of all Available Feature from a camera, this list has been edited Manually for the Features to be grouped and
        sorted.
        This List will not adapt automatically based on the connected camera
        :return:
        """
        with open('data/master_feature_list.csv') as file:
            reader = csv.reader(file)
            list=[]
            for feature in reader:
                list.append(feature)
                #print(feature)
            del list[0]
        return list

    def GetExptime():
        return camera.f.ExposureTime.Get()

    def GetGain():
        return camera.f.Gain.Get()

    def GetFeatureName():
        listname = GetFeatureList()
        for f in listname:
            return f.GetName()

    def SetBinningVertical(BinV):
        """
        NOT USED !!
        Sets the Vertical Binning Value.
        :param BinV:
        :return:
        """
        if BinV > 2:
            print(f"The chosen Gain exceds current limits of:{camera.f.BinningVertical.GetMax()}, Over limit")
        elif BinV < 1:
            print(f"The chosen Gain exceds current limits of {camera.f.BinningVertical.GetMin()}, Negativ Value")
        else:
            camera.f.BinningVertical.Set(BinV)
        return

    def GetBinningVertical():
        return camera.f.BinningVertical.Get()

    def SetBinningHorizontahl(BinH):
        """
        NOT USED!!
        Sets the Horizontal Binning Value
        :return:
        """
        if BinH > 2:
            print("The chosen Gain exceds current limits of 250, Over limit")
        elif BinH < 1:
            print("The chosen Gain exceds current limits of 0, Negativ Value")
        else:
            camera.f.BinningHorizontal.Set(BinH)

    def GetBinningHorizonthal():
        return camera.f.BinningHorizontal.Get()

    def screenshot(cam):
        """
        Connected to the GUI Button Save Frame, Allows to extract the current frame and to save it on the device
        Based on the Color type of the Camera the Format of the Frame has to be Adjusted
        :return: A Numpy array in Qt format
        """
        if cam == "M":
            Capture = camera.GetImage()
            img = Capture.GetNPArray()
            img2 = np.append(img, img, axis=2)
            img3 = np.append(img2, img, axis=2)
            img4 = Image.fromarray(img3, mode='RGB')
        elif cam == "C":
            Capture = camera.GetImage()
            img = Capture.GetNPArray()
            img4 = Image.fromarray(img, mode='RGB')

        qt_img = ImageQt.ImageQt(img4)
        return qt_img

    def frame():
        """
        Returns a Frame from the Baumer Camera
        :return: Numpy array from the frame
        """
        Capture = camera.GetImage()
        img = Capture.GetNPArray()
        return img

    def openSaveDialog():
        """
        Opens the the file manager dialog for saving files
        :return: string path to where the file should be saved
        """
        option = QFileDialog.Options()
        # first param is QWidget
        # second param is Window Title
        # third title is Default File Name
        # fourth param is FileType
        # fifth is options

        # for override native save dialog
        # option|=QFileDialog.DontUseNativeDialog

        file = QFileDialog.getSaveFileName(None, "Save image under", "Screenshot.jpg", "Images (*.png *.xpm *.jpg)",
                                           options=option)
        print(file[0])
        savedialogpath = file[0]
        return savedialogpath

    def openFileDialog():
        """
        Opens the File Manager to choose a file to be opened
        :return: String path of the file to be opened
        """
        option = QFileDialog.Options()
        file = QFileDialog.getOpenFileName(None, "Load Image", "Default File", "All Files(*)", options=option)
        print(file[0])
        opendialogpath = file[0]
        return opendialogpath

    def openMultiFile():
        """
        NOT USED!!
        Possible implementation solution to open multiple file manager windows at once
        :return:
        """
        option = QFileDialog.Options()
        # option |= QFileDialog.DontUseNativeDialog
        file = QFileDialog.getOpenFileNames(widget, "Select Multi File", "default", "All Files (*)", options=option)
        print(file[0])
        return

    def save():
        """
        Function to call in order to save an image
        the function will call fill manager windows and save the file to the specified path
        the Functions checks the Camera Model, in our case if the camera is Monochrom it will send
        "M" back in with Color Camera it will send "C" back
        """
        camerainfolist = neoapi.CamInfoList.Get()
        camerainfolist.Refresh()
        for camerainfo in camerainfolist:
            Camname = camerainfo.GetModelName()
        # savepath = openSaveDialog()
        frame = screenshot(Camname[7])
        frame.save(f"{openSaveDialog()}")

    def OpenImage():
        """
        Function to call for opening a file/ image
        by calling the file manager windows gives back the path where the file is saved and will open it in the default image
        viewer
        """
        try:
            img = Image.open(f"{openFileDialog()}")
            img.show()
        except Exception as e:
            print(type(e))
            traceback.print_exc()

    def autogenerategui(featurename):
        """
        Only Accesisblbe while siging in (see Signin function)
        Function used in GURU mode to access feature of the camera Through the feature List. By choosing a feature the Function
        will check if said feature exists, is available, and writable or readable.
        Once a existing accesible feature has been selected the apropriate input widget will be unlocked in the GUI
        :param featurename: String of the feature to be used
        :return: string type, value, min, max, list of enumeration of the possible strings
        """
        try:
            if not featurename[0] == "*" or "ï":
                if not camera.HasFeature(featurename):
                    val = "Not Available"
                    inter = "Not Available"
                    max, min = 0, 0
                    enumlist = []
                    return val, inter, max, min, enumlist
                if camera.GetFeature(featurename).IsReadable():
                    if camera.GetFeature(featurename).GetInterface() == "IBoolean":
                        print("  Value                   ", camera.GetFeature(featurename).GetBool())
                        val = camera.GetFeature(featurename).GetBool()
                        inter = "bool"
                        max, min = 0, 0
                        enumlist = []
                        return val, inter, max, min, enumlist
                    elif camera.GetFeature(featurename).GetInterface() == "IInteger":
                        print("  ValueString             ", camera.GetFeature(featurename).GetString())
                        val = camera.GetFeature(featurename).GetString()
                        inter = "int"
                        max = camera.GetFeature(featurename).GetIntMax()
                        min = camera.GetFeature(featurename).GetIntMin()
                        enumlist = []
                        return val, inter, max, min, enumlist
                    elif camera.GetFeature(featurename).GetInterface() == "IFloat":
                        print("  ValueString             ", camera.GetFeature(featurename).GetString())
                        val = camera.GetFeature(featurename).GetString()
                        inter = "float"
                        if featurename == "ExposureTime":
                            max = 40000
                            min = 20
                        else:
                            max = camera.GetFeature(featurename).GetIntMax()
                            min = camera.GetFeature(featurename).GetIntMin()
                        enumlist = []
                        return val, inter, max, min, enumlist
                    elif camera.GetFeature(featurename).GetInterface() == "IString":
                        print("  Value                   ", camera.GetFeature(featurename).GetString())
                        val = camera.GetFeature(featurename).GetString()
                        inter = "string"
                        max, min = 0, 0
                        enumlist = []
                        return val, inter, max, min, enumlist
                    elif camera.GetFeature(featurename).GetInterface() == "IEnumeration":
                        print("  Value                   ", camera.GetFeature(featurename).GetString())
                        val = camera.GetFeature(featurename).GetString()
                        inter = "enum"
                        max ,min = 0, 0
                        enumlist = []
                        enumname = camera.GetFeature(featurename).GetEnumValueList()
                        for f in enumname:
                            enumlist.append(f.GetName())
                        return val, inter, max, min, enumlist
                else:
                    val = "Not Available"
                    inter = "Not Available"
                    max, min = 0, 0
                    enumlist = []
                    return val, inter, max, min, enumlist

        except Exception as e:
            print(type(e))
            traceback.print_exc()

    def enumsetter(name, enum):
        """
        After having chosen a  enumeration feature in the GURU feature list, this Function builds the access to the function
        :param name: String
        :param enum: String
        """
        if camera.GetFeature(name).IsWritable():
            camera.SetFeature(name, enum)

    def floatset(name, val):
        """
        After having chosen a float feature in the GURU feature list, this Function builds the access to the function
        :param name: string
        :param val: int, Float is depreciated by Qt, still works tho
        """
        if camera.GetFeature(name).IsWritable():
            camera.SetFeature(name, val)

    def boolset(name, state):
        """
        After having chosen a boolean feature in the GURU feature list, this Function builds the access to the function
        :param name: String
        :param state: bool
        """
        if camera.GetFeature(name).IsWritable():
            camera.SetFeature(name, state)

    def featuredescrpition(featurename):
        """
        After having chosen a feature in the GURU feature list, this Function calls the neoAPI description of the function
        :param featurename: String
        :return: String
        """
        Desc = camera.GetFeature(featurename).GetDescription()
        return Desc

except Exception as e:
    print(type(e))
    traceback.print_exc()
