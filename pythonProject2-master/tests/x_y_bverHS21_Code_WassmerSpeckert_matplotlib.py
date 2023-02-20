"""
Image preprocessing für weitere Verarbeitung im Algorithmus
"""

# *************************************************************
# Imports
# *************************************************************

import cv2
import numpy as np
import FeatureControle
import matplotlib.pyplot as plt

window = '2D-Array'  # Name des Anzeigefensters
global points
points = []
  # Globale Liste für zugriff aus Callback-Funktion
global measPoints
measpoints= []
path = '../bilder/20220113_000_Anwesend_2.jpg'
fig = plt.figure()


# *************************************************************
# Perspektivische Korrektur
# Quelle: https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/
# *************************************************************


def order_points(pts):
    # initialzie a list of coordinates that will be ordered
    # such that the first entry in the list is the top-left,
    # the second entry is the top-right, the third is the
    # bottom-right, and the fourth is the bottom-left
    rect = np.zeros((4, 2), dtype="float32")
    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    diff = np.diff(pts, axis=1)
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

    # get min value
    minY = min(tl[1], tr[1], br[1], bl[1])
    minX = min(tl[0], tr[0], br[0], bl[0])

    # shift whole rectangel to max left up
    shiftLeftUp = (minX, minY)
    tl = tl - shiftLeftUp
    tr = tr - shiftLeftUp
    br = br - shiftLeftUp
    bl = bl - shiftLeftUp

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

    # Skalierungsfaktor berechnen
    # x-Richtung
    factorX = image.shape[1] / maxWidth

    # y-Richtung
    factorY = image.shape[0] / maxHeight

    factor = factorX  # min(factorX, factorY)

    tl = tl * factor
    tr = tr * factor
    br = br * factor
    bl = bl * factor

    rectNew = (tl, tr, br, bl)

    rectNew = np.array(rectNew, dtype=np.float32)

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
        [0, maxHeight - 1]], dtype="float32")

    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rectNew, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    # return the warped image
    return warped


# *************************************************************
# Rechteck auswählen durch 4 Punkte
# 4 Quadrate werden am Anfang generiert, diese söllen die Rände des MessAray representieren
# Bei jedem CLick wird diese Function aufgerüfen
# *************************************************************
def click_event(event):
    global points
    xi, yi = event.xdata, event.ydata
    print(xi)
    xi = round(xi, 0)
    yi = round(yi, 0)
    xi = int(xi)
    yi = int(yi)
    event = 1
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # if event == plt.waitforbuttonpress:
        # append coordinates to global list
        points.append([xi, yi])

        #imgpoint2 = np.ascontiguousarray(img, dtype=np.uint8)
        imgpoint2 = np.copy(img)
        imgpoint3 = cv2.rectangle(imgpoint2, [xi + 10, yi + 10], [xi - 10, yi - 10], [0, 0, 0], -1)
        # cv2.imshow(window, imgpoint3)
        plt.imshow(imgpoint3)
        plt.show()


# *************************************************************
# Messpunkte auswählen
# *************************************************************
def click_event_meas(event):
    global measPoints
    xi, yi = event.xdata, event.ydata
    event = 1
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # append coordinates to global list
        measPoints.append([xi, yi])

        warped1 = np.ascontiguousarray(warped, dtype=np.uint8)
        warped2 = cv2.circle(warped1, (xi, yi), 5, [0, 255, 0], -1)
        # cv2.imshow(window, warped2)
        plt.imshow(warped2)
        plt.show()


# *************************************************************
# Koordinaten ermitteln
# Quelle: https://www.examplefiles.net/cs/1251957
# *************************************************************
def getCoordinates(coorimg):
    coordinates = []

    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = coorimg
    retVal, binary = cv2.threshold(gray, 0, 15, cv2.THRESH_BINARY_INV)
    blur = cv2.GaussianBlur(binary, (7, 7), 0.5)
    edge = cv2.Canny(blur, 0, 50, 3)

    # Konturen finden
    cnts = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    # Rechtecke um gefundene Konturen zeichnen
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)

        # Grösse filtern, sodass nur die gewünschten Rechtecke markiert werden
        if (w > 0 and w < 100) and (h > 0 and h < 100):
            print('W= {}, H= {}'.format(w, h))
            cv2.rectangle(coorimg, (x, y), (x + w, y + h), (36, 255, 12), 2)
            coordinates.append((x, y))

    return coordinates, coorimg


# ***********************************************************
# Distanz berechnen
# Quelle: https://stackoverflow.com/questions/57313708/distance-between-two-points-in-opencv-based-on-known-measurement
# ***********************************************************
def calculateDistance(refPoints: list, measurePoints: list):
    """ Gibt die Distanz zwischen den beiden Messpunkten zurück.
		für die Berechnung werden vier sortierte Referenzpunkte benötigt.
	"""
    # Referenzpunkte sortieren
    pts = np.array(refPoints, dtype=np.float32)
    ref = order_points(pts)
    (tl, tr, br, bl) = ref

    # Messpunkte
    (m1, m2) = measurePoints

    # Pixeldistanz der Messpunkte (Euklid):
    distMeas = np.sqrt(((m1[0] - m2[0]) ** 2) + ((m1[1] - m2[1]) ** 2))
    distx = abs(m1[0] - m2[0])
    disty = abs(m1[1] - m2[1])
    # Pixeldistanz der Referenzpunkte(Euklid):
    distRef = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))

    # Distanz pro Pixel berechnen (kleines Quadrat ist 100*100mm)
    ratio = 100 / distRef
    resx = distx * ratio
    resy = disty * ratio
    # Damit die daten lesbarer sind werden sie auf den 2. zehntellt ausgerundet
    nresx = round(resx, 2)
    nresy = round(resy, 2)

    dist = [nresx, nresy]

    return dist


def offsetread():
    # *************************************************************
    # Ablauf
    # *************************************************************
    global img
    global warped
    global p
    # img = cv2.imread(path)
    img = FeatureControle.frame()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Eingelesenes Bild anzeigen
    # cv2.imshow(window, img)
    plt.imshow(img)
    plt.show()

    # 4 Punkte auswählen
    # cv2.setMouseCallback(window, click_event)
    fig.canvas.mpl_connect('button_press_event', click_event)

    # Warten auf Tastendruck
    # cv2.waitKey(0)
    #plt.waitforbuttonpress()
    fig.canvas.mpl_connect('button_key_event', seconde)


def seconde():
    # Perspektivische Korrektur mit gewählten Punkten
    warped = four_point_transform(img, points)

    # cv2.imshow(window, warped)
    plt.imshow(warped)
    plt.show()

    # Neue Koordinaten der 4 gezeichneten Punkte bestimmen
    newPoints, newimg = getCoordinates(warped)

    print(newPoints)

    # Warten auf Tastendruck
    # cv2.waitKey(0)
    plt.waitforbuttonpress(0)

    # cv2.imshow(window, newimg)
    plt.imshow(newimg)
    plt.show()

    # 2 Punkte auswählen
    # cv2.setMouseCallback(window, click_event_meas)
    fig.canvas.mpl_connect('button_press_event', click_event_meas)

    # Warten auf Tastendruck
    # cv2.waitKey(0)
    plt.waitforbuttonpress(0)

    distance = calculateDistance(points, measPoints)

    # Linie zwischen Messpunkten Zeichnen
    lineThickness = 1
    (m1, m2) = measPoints
    m12 = [m2[0], m1[1]]

    cv2.line(newimg, m1, m12, (0, 0, 255), lineThickness)
    cv2.line(newimg, m12, m2, (0, 0, 255), lineThickness)

    # Distanz auf Bild anzeigen
    cv2.putText(newimg, 'U ~= {}mm'.format(distance[0]), m1, cv2.FONT_HERSHEY_SIMPLEX, 2, 255, 2)
    cv2.putText(newimg, 'T ~= {}mm'.format(distance[1]), m2, cv2.FONT_HERSHEY_SIMPLEX, 2, 255, 2)

    # cv2.imshow(window, newimg)
    plt.imshow(newimg)
    plt.show()
    # Warten auf Tastendruck
    cv2.waitKey(0)

    # cv2.imwrite('res_{}'.format(path),img)

    # Fenster schliessen
    cv2.destroyAllWindows()

    return distance
