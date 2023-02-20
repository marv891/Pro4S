import neoapi


camera = neoapi.Cam()
camera.Connect()
#neoapi.CamBase.GetFeatureList()
list = camera.GetFeatureList()
print(list)
for f in list:
    #print(f"{f.GetName()} hat den wert.. {f.GetValue()}")
    print(f"{f.GetName()}")
    print(f"Description: {f.GetDescription()}")
