# 002_CameraFeatureList.py
# pip install D:\Baumer\neoAPI120_2120\Baumer_neoAPI_1.2.0_win_x86_64_python\wheel\neoapi-1.2.0-cp36-cp36m-win_amd64.whl

import sys
import neoapi

bSelectCamera = True  # False = 1st camera


def IPv4ToString(IP):
    ipaddressstring = "{}.{}.{}.{}".format(((IP & 0xff000000) >> 24), ((IP & 0x00ff0000) >> 16),
                                           ((IP & 0x0000ff00) >> 8), (IP & 0x0000ff))
    return ipaddressstring


def printCameraFeatureInformation(camera, featurename):
    try:
        print("  Interface               ", camera.GetFeature(featurename).GetInterface())
        print("  Name                    ", camera.GetFeature(featurename).GetName())
        print("  DisplayName             ", camera.GetFeature(featurename).GetDisplayName())
        print("  Description             ", camera.GetFeature(featurename).GetDescription())
        print("  ToolTip                 ", camera.GetFeature(featurename).GetToolTip())
        print("  Visibility              ", camera.GetFeature(featurename).GetVisibility())

        print("  IsAvailable             ", camera.GetFeature(featurename).IsAvailable())
        print("  IsReadable              ", camera.GetFeature(featurename).IsReadable())
        print("  IsWritable              ", camera.GetFeature(featurename).IsWritable())
        print("  IsSelector              ", camera.GetFeature(featurename).IsSelector())
        if camera.GetFeature(featurename).IsAvailable() == True and camera.GetFeature(featurename).IsReadable() == True:
            if camera.GetFeature(featurename).GetInterface() == "IBoolean":
                print("  Value                   ", camera.GetFeature(featurename).GetBool())

            elif camera.GetFeature(featurename).GetInterface() == "IInteger":
                print("  ValueString             ", camera.GetFeature(featurename).GetString())
                print("  Int                     ", camera.GetFeature(featurename).GetInt())
                print("  IntMin                  ", camera.GetFeature(featurename).GetIntMin())
                print("  IntMax                  ", camera.GetFeature(featurename).GetIntMax())
                print("  IntInc                  ", camera.GetFeature(featurename).GetIntInc())
                print("  Representation          ", camera.GetFeature(featurename).GetRepresentation())
                print("  Unit                    ", camera.GetFeature(featurename).GetUnit())

            elif camera.GetFeature(featurename).GetInterface() == "IFloat":
                print("  ValueString             ", camera.GetFeature(featurename).GetString())
                print("  Double                  ", camera.GetFeature(featurename).GetDouble())
                print("  DoubleMin               ", camera.GetFeature(featurename).GetDoubleMin())
                print("  DoubleMax               ", camera.GetFeature(featurename).GetDoubleMax())
                print("  DoublePrecision         ", camera.GetFeature(featurename).GetDoublePrecision())
                print("  DoubleInc               ", camera.GetFeature(featurename).GetDoubleInc())
                print("  Unit                    ", camera.GetFeature(featurename).GetUnit())

            elif camera.GetFeature(featurename).GetInterface() == "IString":
                print("  Value                   ", camera.GetFeature(featurename).GetString())
                print("  MaxStringLength         ", camera.GetFeature(featurename).GetMaxStringLength())

            elif camera.GetFeature(featurename).GetInterface() == "IEnumeration":
                print("  Value                   ", camera.GetFeature(featurename).GetString())
                print("  Value (Integer)         ", camera.GetFeature(featurename).GetInt())
                print("  Enumeration Count       ", camera.GetFeature(featurename).GetEnumValueList().GetSize())
                index = 0
                for enumfeature in camera.GetFeature(featurename).GetEnumValueList():
                    if enumfeature.IsAvailable() and enumfeature.IsReadable():
                        print('                     [{:2d}]  '.format(index), end="")
                        print('{:30s}'.format(enumfeature.GetString()), end="")
                        print(' ({:d})'.format(enumfeature.GetInt()))
                    index = index + 1

        if camera.GetFeature(featurename).IsSelector() == True:
            print("  SelectedFeatureList     ", camera.GetFeature(featurename).GetSelectedFeatureList().GetSize())
            selectedfeatures = camera.GetFeature(featurename).GetSelectedFeatureList()
            for selectedfeature in selectedfeatures:
                if selectedfeature.IsReadable() == True:
                    print("                         * ", end="")
                else:
                    print("                           ", end="")
                print(selectedfeature.GetName(), end="")
                print(" ")

    except (neoapi.NeoException) as exc:
        print('error: ', exc.GetDescription())
    return


result = 0

print("+--------------------------+")
print("| 002_CameraFeatureList.py |")
print("+--------------------------+")
print("")

try:

    print("neoapi version:", neoapi.CamBase.GetLibraryVersion())
    print("Python version:", sys.version)
    # print("Numpy version:", np.__version__)
    print("")

    # List of cameras
    cameraId = ""
    cameraIds = []

    camerainfolist = neoapi.CamInfoList.Get()
    camerainfolist.Refresh()

    for camerainfo in camerainfolist:
        cameraname = camerainfo.GetModelName() + "_" + camerainfo.GetSerialNumber()
        print(' [{:2d}]'.format(len(cameraIds) + 1), '{:27s}'.format(cameraname), end="")
        if camerainfo.GetTLType() == "GEV":
            print(' at {:s}'.format(camerainfo.GetGevIpAddress()), end="")
        elif camerainfo.GetTLType() == "U3V":
            print(' at {:s}'.format(camerainfo.GetUSBPortID()), end="")
        print("")
        cameraIds.append(camerainfo.GetId())
        # cameraIds.append(camerainfo.GetSerialNumber())
    print("")

    # SELECT A CAMERA
    KeyDeviceSelector = 1
    if bSelectCamera == True:
        # print(" Select a camera [1 to", '{}, 0 for none]: '.format(len(cameraIds)))
        KeyDeviceSelector = int(input(" Select a camera [1 to" + ' {}, 0 for none]: '.format(len(cameraIds))))
        print("")
    if (KeyDeviceSelector > 0) & (KeyDeviceSelector <= len(cameraIds)):
        cameraId = cameraIds[KeyDeviceSelector - 1]
    else:
        x = input("Input any number to stop: ")
        sys.exit(result)

    camera = neoapi.Cam()
    camera.Connect(cameraId)
    # camera.Connect()
    if camera.IsConnected():
        # print("Camera: " + camera.f.DeviceModelName.GetString() + "_" + camera.f.DeviceSerialNumber.GetString(), camera.f.DeviceFirmwareVersion.GetString())
        print("Camera: " + camera.GetInfo().GetModelName() + "_" + camera.GetInfo().GetSerialNumber(), end="")
        if camera.HasFeature("DeviceFirmwareVersion"):
            print(" " + camera.f.DeviceFirmwareVersion.GetString(), end="")
        elif camera.HasFeature("DeviceManufacturerInfo"):
            print(" " + camera.f.DeviceManufacturerInfo.GetString(), end="")
        if camera.HasFeature("DeviceVersion"):
            print(" " + camera.f.DeviceVersion.GetString(), end="")
        print("")

        # System info
        print("  TLID                           ", camera.GetRuntimeInfoList()["TLID"].GetString())

        # ExposureAuto
        if camera.HasFeature("ExposureAuto"):
            if camera.IsWritable("ExposureAuto"):
                camera.SetFeature("ExposureAuto", "Off")
                print("  ExposureAuto                   ", camera.GetFeature("ExposureAuto").GetString())
        print(camera.HasFeature("ExposureAuto"))

        # feature list
        print("Camera Parameters ")
        print("  FeatureList.Size               ", camera.GetFeatureList().GetSize())
        print("  ")
        # features = camera.GetFeatureList()
        # for feature in features:
        #     # if (feature.IsAvailable() and feature.IsImplemented()):
        #     if (feature.IsAvailable()):
        #         print( "  [" + '{:12s}'.format(feature.GetInterface()) + "]  ", end="")
        #         print('{:42s}'.format(feature.GetName()) + ": ", end="")
        #         if feature.IsReadable():
        #             print(feature.GetString(), end="")
        #         print("")
        # print("")
        #
        featurenames = []
        features2 = camera.GetFeatureList()
        for feature in features2:
            if (feature.IsAvailable()):
                featurenames.append(feature.GetName())
        print("  FeatureList.Sorted ")
        featurenames.sort()
        for featurename in featurenames:
            print("  [" + '{:12s}'.format(camera.GetFeature(featurename).GetInterface()) + "]  ", end="")
            print('{:42s}'.format(camera.GetFeature(featurename).GetName()) + ": ", end="")
            if camera.GetFeature(featurename).IsReadable():
                print(camera.GetFeature(featurename).GetString(), end="")
            print("")
        print("")

        # Feature details
        print("Feature Details ")
        sFeature = "TriggerSource"
        while sFeature != "exit":
            print("  ")
            printCameraFeatureInformation(camera, sFeature)
            sFeature = input("input name of the camera feature like 'ExposureTime' or 'exit' to stop: \n\r")
        print("")

except (neoapi.NeoException) as exc:
    print('error: ', exc.GetDescription())
    result = 1

x = input("Input any number to stop: ")
sys.exit(result)
