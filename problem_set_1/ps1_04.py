import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math as math

def hsiToBGR(colorHSI):
    colorBGR = [0, 0, 0]
    HSI = colorHSI.copy()
    if(colorHSI[1]==0):
        colorBGR = [HSI[1], HSI[1], HSI[1]]
    else:
        if(HSI[0]<2*math.pi/3):
            colorBGR[0] = 255*HSI[2]*(1-HSI[1])
            colorBGR[1] = 255*HSI[2]*(1+HSI[1]*math.cos(2*math.pi/3-HSI[0])/(math.cos(math.pi/3-HSI[0])))
            colorBGR[2] = 255*HSI[2]*(1+HSI[1]*math.cos(HSI[0])/(math.cos(math.pi/3-HSI[0])))
        elif(HSI[0]<4*math.pi/3):
            HSI[0] -= 2*math.pi/3
            colorBGR[2] = 255*HSI[2]*(1-HSI[1])
            colorBGR[0] = 255*HSI[2]*(1+HSI[1]*math.cos(2*math.pi/3-HSI[0])/(math.cos(math.pi/3-HSI[0])))
            colorBGR[1] = 255*HSI[2]*(1+HSI[1]*math.cos(HSI[0])/(math.cos(math.pi/3-HSI[0])))
        else:
            HSI[0] -= 4*math.pi/3
            colorBGR[1] = 255*HSI[2]*(1-HSI[1])
            colorBGR[2] = 255*HSI[2]*(1+HSI[1]*math.cos(2*math.pi/3-HSI[0])/(math.cos(math.pi/3-HSI[0])))
            colorBGR[0] = 255*HSI[2]*(1+HSI[1]*math.cos(HSI[0])/(math.cos(math.pi/3-HSI[0])))
    return colorBGR

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    if (phi<0):
        phi = 2*math.pi+phi
    return rho, phi

intensidade = input("Digite seu valor de intensidade (0-255)")
intensidade = float(intensidade)
HSI = [0, 0, 0]
HSI[2] = intensidade/255
x = 0
y = 0
i = 0
j = 0
w = 601
img = np.zeros((w,w,3), np.uint8)
simg = np.zeros((w,w,3), np.uint8)
color = [0, 0, 0]
for i in range(0,w):
    for j in range(0,w):
        color = [0, 0, 0]
        HSI[0] = 0
        HSI[1] = 0
        x = (i - 301)/(301)
        y = -(j - 301)/(301)
        r, theta = cart2pol(x, y)
        if(r<=1):
            HSI[1] = r
            HSI[0] = theta
            color = hsiToBGR(HSI.copy())
        if((color[0]+color[1]+color[2])/3<intensidade-2):
            color = [0, 0, 0]
        img[j, i] = color
        simg[j, i] = HSI[1]*255
        if(x==0 and y==0):
            img[j, i] = [intensidade, intensidade, intensidade]
        j+=1
    j=0
    i+=1

cv.imshow("HSI Planar Cut", img)
cv.imshow("HSI Planar Cut S", simg)
cv.waitKey()