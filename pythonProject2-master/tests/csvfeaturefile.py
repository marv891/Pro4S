import csv
import neoapi

camera = neoapi.Cam()
camera.Connect()
list = camera.GetFeatureList()
Listcsv = []

for a in list:
    Listcsv.append(a.GetName())
with open('psifeatures.csv', 'w', newline='') as f:

    writer = csv.writer(f)

    for b in Listcsv:
        writer.writerow([b])
