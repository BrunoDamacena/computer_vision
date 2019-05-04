import cv2
from matplotlib import pyplot as plt
import numpy as np

plt.figure(num='Original Histogram')
img = cv2.imread('image.png', 0)
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'g')
plt.hist(img.flatten(), 256, [0, 256], color = 'r')
plt.xlim([0, 256])
cv2.imshow('Original Image', img)
plt.legend(('Cumulative Distribution Function', 'Histogram'), loc = 'upper left')
plt.show()
plt.close()

r = 0
plt.figure(num='Equalized Histogram')
equ = cv2.equalizeHist(img)
cv2.imwrite("equalized_image.png", equ)
hist,bins = np.histogram(equ.flatten(),256,[0,256])
cdf = hist.cumsum() ** r
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'g')
plt.hist(equ.flatten(), 256, [0, 256], color = 'r')
plt.xlim([0, 256])
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
equ = cdf[equ]
cv2.imshow('Equalized Image', equ)
plt.legend(('Cumulative Distribution Function', 'Histogram'), loc = 'upper left')
plt.show()
cv2.waitKey()

cv2.imwrite('equalized_r_' + str(r) + '.png', equ)