import cv2 as cv
import numpy as np
import math
import sys

def draw_random_lines(img, w, n):
    for i in range(n):
        point1 = (np.random.randint(low = 0, high = w), np.random.randint(low = 0, high = w))
        point2 = (np.random.randint(low = 0, high = w), np.random.randint(low = 0, high = w))
        cv.line(img,point1,point2,(255,0,0),5)
    x = y = 0
    while(y<w):
        while(x<w):
            if(np.any(img[x, y] != 0)):
                if(np.random.randint(low=0, high=100) < 60):
                    img[x, y] = [255, 255, 255] 
                else:
                    img[x, y] = [0, 0, 0]
            else:
                if(np.random.randint(low=0, high=100) < 95):
                    img[x, y] = [255, 255, 255] 
                else:
                    img[x, y] = [130, 130, 130]
            x+=1
        x=0
        y+=1
    return img

w = 512
img = np.zeros((w,w,3), np.uint8)
img = draw_random_lines(img, w, 5)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
dst = cv.Canny(gray, 140, 255, None, 3)

cv.imshow("Source", gray)
cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
cdstP = np.copy(cdst)

linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)

if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)


cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)

cv.waitKey()