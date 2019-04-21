import cv2
from matplotlib import pyplot as plt
import numpy as np

plt.figure(num='Original Histogram')
img = cv2.imread('image.png', 0)
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(), 256, [0, 256], color = 'r')
plt.xlim([0, 256])
cv2.imshow('Original Image', img)
plt.legend(('Cumulative Distribution Function', 'histogram'), loc = 'upper left')
plt.show()
plt.close()

plt.figure(num='Equalized Histogram')
r = 1
equ = cv2.equalizeHist(img*(2**r))
hist,bins = np.histogram(equ.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(equ.flatten(), 256, [0, 256], color = 'r')
plt.xlim([0, 256])
cv2.imshow('Equalized Image', equ)
plt.legend(('Cumulative Distribution Function', 'histogram'), loc = 'upper left')
plt.show()
cv2.waitKey()