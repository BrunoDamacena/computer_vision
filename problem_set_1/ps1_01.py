import cv2
from matplotlib import pyplot
import numpy

pyplot.figure(num='Homogeneous')
img = cv2.imread('solid.png')

def showParameters(x,y):
    color = img[y,x]
    intensity = numpy.average(color)
    mean = numpy.average(img[y-5:y+5, x-5:x+5])
    standartDeviation = numpy.std(img[y-5:y+5, x-5:x+5])
    print('Position:', (x,y))
    print('Color: ', color)
    print('Intensity: ', intensity)
    print('Mean: ', mean)
    print('Standart Deviation: ', standartDeviation)
    
def printRectangle(x,y,imgToShow):
    pt1 = (x-5, y-5)
    pt2 = (x+5, y+5)
    cv2.rectangle(imgToShow, pt1, pt2, (255,0,0), 1)
    cv2.imshow('Image', imgToShow)

def onMouseMovement(event,x,y,flags,param):
    if(event == cv2.EVENT_MOUSEMOVE):
        imgToShow = img.copy()
        printRectangle(x,y,imgToShow)
        showParameters(x,y)     

cv2.imshow('Image', img)
cv2.setMouseCallback('Image', onMouseMovement)

for i, col in enumerate(('b','g','r')):
    histogram = cv2.calcHist([img], [i], None, [256], [0,256])
    pyplot.plot(histogram,col)
pyplot.show()

cv2.waitKey()

