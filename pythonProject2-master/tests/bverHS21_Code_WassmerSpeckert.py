"""
Image preprocessing für weitere Verarbeitung im Algorithmus
"""

#*************************************************************
#Imports
#*************************************************************

import cv2
import numpy as np

#*************************************************************
#Perspektivische Korrektur
#Quelle: https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/
#*************************************************************
def order_points(pts):
	# initialzie a list of coordinates that will be ordered
	# such that the first entry in the list is the top-left,
	# the second entry is the top-right, the third is the
	# bottom-right, and the fourth is the bottom-left
	rect = np.zeros((4, 2), dtype = "float32")
	# the top-left point will have the smallest sum, whereas
	# the bottom-right point will have the largest sum
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]
	# now, compute the difference between the points, the
	# top-right point will have the smallest difference,
	# whereas the bottom-left will have the largest difference
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
	# return the ordered coordinates
	return rect

def four_point_transform(image, pts):
	# obtain a consistent order of the points and unpack them
	# individually
	pts = np.array(pts, dtype=np.float32)
	rect = order_points(pts)
	(tl, tr, br, bl) = rect

	#get min value
	minY = min(tl[1], tr[1], br[1],bl[1])
	minX = min(tl[0], tr[0], br[0], bl[0])
	
	#shift whole rectangel to max left up
	shiftLeftUp = (minX, minY)
	tl = tl-shiftLeftUp
	tr = tr-shiftLeftUp
	br = br-shiftLeftUp
	bl = bl-shiftLeftUp

	# compute the width of the new image, which will be the
	# maximum distance between bottom-right and bottom-left
	# x-coordiates or the top-right and top-left x-coordinates
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))
	# compute the height of the new image, which will be the
	# maximum distance between the top-right and bottom-right
	# y-coordinates or the top-left and bottom-left y-coordinates
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))
	
	#Skalierungsfaktor berechnen
	# x-Richtung
	factorX = image.shape[1] / maxWidth

	# y-Richtung
	factorY = image.shape[0] / maxHeight

	factor = factorX #min(factorX, factorY)
	
	tl = tl * factor
	tr = tr * factor
	br = br * factor
	bl = bl * factor

	rectNew = (tl, tr, br, bl)

	rectNew = np.array(rectNew, dtype= np.float32)
	
	# compute the width of the new image, which will be the
	# maximum distance between bottom-right and bottom-left
	# x-coordiates or the top-right and top-left x-coordinates
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))
	# compute the height of the new image, which will be the
	# maximum distance between the top-right and bottom-right
	# y-coordinates or the top-left and bottom-left y-coordinates
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))


	# now that we have the dimensions of the new image, construct
	# the set of destination points to obtain a "birds eye view",
	# (i.e. top-down view) of the image, again specifying points
	# in the top-left, top-right, bottom-right, and bottom-left
	# order
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")
	
	# compute the perspective transform matrix and then apply it	
	M = cv2.getPerspectiveTransform(rectNew, dst)	
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
	
    # return the warped image
	return warped


#*************************************************************
#Rechteck auswählen durch 4 Punkte
#*************************************************************
def click_event(event, x, y, flags, params):
	global points, img

	# checking for left mouse clicks
	if event == cv2.EVENT_LBUTTONDOWN:

		#append coordinates to global list
		points.append([x,y])

		img = np.ascontiguousarray(img, dtype=np.uint8)
		img = cv2.rectangle(img, [x+10,y+10], [x-10,y-10],[0,0,0],-1)
		cv2.imshow(window, img)

#*************************************************************
#Messpunkte auswählen
#*************************************************************
def click_event_meas(event, x, y, flags, params):
	global measPoints, img

	# checking for left mouse clicks
	if event == cv2.EVENT_LBUTTONDOWN:

		#append coordinates to global list
		measPoints.append([x,y])

		warped = np.ascontiguousarray(img, dtype=np.uint8)
		warped = cv2.circle(warped, (x,y),5, [0,255,0], -1)
		cv2.imshow(window, img)


#*************************************************************
#Koordinaten ermitteln
#Quelle: https://www.examplefiles.net/cs/1251957
#*************************************************************
def getCoordinates(img):
	
	coordinates = []
	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	retVal ,binary = cv2.threshold(gray,0,15,cv2.THRESH_BINARY_INV)
	blur = cv2.GaussianBlur(binary, (7, 7), 0.5)
	edge = cv2.Canny(blur, 0, 50, 3)

	#Konturen finden
	cnts = cv2.findContours(edge,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if len(cnts) == 2 else cnts[1]

	# Rechtecke um gefundene Konturen zeichnen
	for c in cnts:
		x,y,w,h = cv2.boundingRect(c)

		#Grösse filtern, sodass nur die gewünschten Rechtecke markiert werden
		if (w > 19 and w < 23) and (h > 17 and h < 23):
			print('W= {}, H= {}'.format(w,h))
			cv2.rectangle(img, (x, y), (x + w, y + h), (36,255,12), 2)
			coordinates.append((x,y))
	
	return coordinates, img

#***********************************************************
#Distanz berechnen
#Quelle: https://stackoverflow.com/questions/57313708/distance-between-two-points-in-opencv-based-on-known-measurement
#***********************************************************
def calculateDistance(refPoints: list, measurePoints: list):
	""" Gibt die Distanz zwischen den beiden Messpunkten zurück.
		für die Berechnung werden vier sortierte Referenzpunkte benötigt.
	"""
	#Referenzpunkte sortieren
	pts = np.array(refPoints, dtype=np.float32)
	ref = order_points(pts)
	(tl, tr, br, bl) = ref

	#Messpunkte
	(m1,m2) = measurePoints

	#Pixeldistanz der Messpunkte (Euklid):
	distMeas = np.sqrt(((m1[0] - m2[0]) ** 2) + ((m1[1] - m2[1]) ** 2))

	#Pixeldistanz der Referenzpunkte(Euklid):
	distRef = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))

	#Distanz pro Pixel berechnen (kleines Quadrat ist 100*100mm)
	ratio = 100/distRef

	res = distMeas * ratio
	res = round(res,2)

	return res
	
        
#*************************************************************
#Ablauf
#*************************************************************
window = '2D-Array' #Name des Anzeigefensters
points= [] #Globale Liste für zugriff aus Callback-Funktion
measPoints = []

path = '../bilder/20220113_000_Anwesend_2.jpg'
#path = 'img_20220201_185633.jpg'


#Bild einlesen
img = cv2.imread(path)

#Eingelesenes Bild anzeigen
cv2.imshow(window,img)

#4 Punkte auswählen
cv2.setMouseCallback(window, click_event)

#Warten auf Tastendruck
cv2.waitKey(0)

#Perspektivische Korrektur mit gewählten Punkten
warped = four_point_transform(img, points)

cv2.imshow(window, warped)

#Neue Koordinaten der 4 gezeichneten Punkte bestimmen
newPoints, img = getCoordinates(warped)

print(newPoints)

#Warten auf Tastendruck
cv2.waitKey(0)

cv2.imshow(window, img)

#2 Punkte auswählen
cv2.setMouseCallback(window, click_event_meas)

#Warten auf Tastendruck
cv2.waitKey(0)

distance = calculateDistance(points, measPoints)

#Linie zwischen Messpunkten Zeichnen
lineThickness = 1
(m1,m2) = measPoints
cv2.line(img, m1, m2, (0,0,255), lineThickness)
#Distanz auf Bild anzeigen
cv2.putText(img,'L = {}mm'.format(distance), m1, cv2.FONT_HERSHEY_SIMPLEX, 3, 255)

cv2.imshow(window,img)

#Warten auf Tastendruck
cv2.waitKey(0)

#cv2.imwrite('res_{}'.format(path),img)

#Fenster schliessen
cv2.destroyAllWindows()


