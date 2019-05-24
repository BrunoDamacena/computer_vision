import numpy as np
import cv2
import sys
from matplotlib import pyplot as plt

sys.setrecursionlimit(1440)

def label_adj8(x, y, img, number, labels, target):
  x_min = (x - 1) if (x - 1) >= 0 else 0
  x_max = (x + 1) if (x + 1) < len(img) else len(img) - 1
  y_min = (y - 1) if (y - 1) >= 0 else 0
  y_max = (y + 1) if (y + 1) < len(img[x]) else len(img[x]) - 1

  for i in range(x_min, x_max + 1):
    for j in range(y_min, y_max + 1):
      if i != x or j != y:
        if img[i, j] == target and labels[i, j] == 0:
          labels[i, j] = number
          label_adj8(i, j, img, number, labels, target)

def count_components(img, labels, black_over_white = True):
  target = 0 if black_over_white else 255
  count = 0
  for i in range(0, len(img)):
    for j in range(0, len(img[i])):
      if img[i, j] == target:
        if labels[i, j] == 0:
          count = count + 1
          labels[i, j] = count
          label_adj8(i, j, img, count, labels, target)
  return count
  
def show_label_info(event,x,y,flags,labels):
  if event == cv2.EVENT_LBUTTONDOWN:
    print("X: {} Y: {} Label: {}".format(x,y,labels[y,x]))
    a = 0
    print("Label area: {}".format((labels == labels[y,x]).sum()))
  

T = 230
I = cv2.imread('pills.jpg', cv2.IMREAD_GRAYSCALE)
_,J = cv2.threshold(I, T, 255, cv2.THRESH_BINARY)


labels = np.zeros((len(J), len(J[0])))
print("Number of components found: {}".format(count_components(J, labels)))

cv2.imshow('Threshold image',J)
cv2.imwrite('thresholdimage.jpg', J)
cv2.setMouseCallback('Threshold image', show_label_info, labels)
cv2.waitKey(0)
