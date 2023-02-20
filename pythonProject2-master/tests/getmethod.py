import neoapi

camera = neoapi.Cam()
camera.Connect()


def getoffset():
    return camera.f.OffsetX.Get()
def setoffset(newoff):
    camera.f.OffsetX.Set(newoff)

    return

print(camera.f.OffsetX.GetInc())