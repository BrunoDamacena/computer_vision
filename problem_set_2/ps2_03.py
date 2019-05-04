import cv2
import numpy as np

img = cv2.imread("prego.jpg", 0)
img = cv2.resize(img, (640,480))

fourierTransform = np.fft.fft2(img)
amplitude = np.absolute(fourierTransform)
phase = np.angle(fourierTransform)

amplitudeImage = np.ndarray.astype(np.absolute(np.fft.ifft2(amplitude*(np.sin(phase)*1j))), np.uint8)
phaseImage = np.ndarray.astype(np.absolute(np.fft.ifft2(amplitude*(np.cos(phase)))), np.uint8)

cv2.imshow("amp", amplitudeImage)
cv2.imshow("phase", phaseImage)

cv2.waitKey()