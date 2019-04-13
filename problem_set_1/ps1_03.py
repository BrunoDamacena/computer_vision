import cv2
from matplotlib import pyplot
import numpy

img1 = cv2.imread('01_03_01.jpg', 0)
img2 = cv2.imread('01_03_02.jpg', 0)

fourierTransform = numpy.fft.fft2(img1)
amplitude1 = numpy.absolute(fourierTransform)
phase1 = numpy.angle(fourierTransform)

fourierTransform = numpy.fft.fft2(img2)
amplitude2 = 0.5 * numpy.absolute(fourierTransform)
phase2 = numpy.angle(fourierTransform)

# a)
img4 = amplitude2*(numpy.sin(phase1)*1j + numpy.cos(phase1))
img3 = amplitude1*(numpy.sin(phase2)*1j + numpy.cos(phase2))

img3 = numpy.ndarray.astype(numpy.absolute(numpy.fft.ifft2(img3)), numpy.uint8)
img4 = numpy.ndarray.astype(numpy.absolute(numpy.fft.ifft2(img4)), numpy.uint8)

cv2.imshow('Amplitude from Image 1, Phase from Image 2', img3)
cv2.imshow('Amplitude from Image 2, Phase from Image 1', img4)
cv2.waitKey()

cv2.destroyAllWindows()

# b)
amplitude = 0.5 * amplitude2
phase = phase2
img5 = amplitude*(numpy.sin(phase2)*1j + numpy.cos(phase2))
img6 = amplitude2*(numpy.sin(phase)*1j + numpy.cos(phase))
img5 = numpy.ndarray.astype(numpy.absolute(numpy.fft.ifft2(img5)), numpy.uint8)
img6 = numpy.ndarray.astype(numpy.absolute(numpy.fft.ifft2(img6)), numpy.uint8)
cv2.imshow('Original Image', img2)
cv2.imshow('Aplitude Changed Image', img5)
cv2.imshow('Phase Changed Image', img6)
cv2.waitKey()

cv2.destroyAllWindows()

# c)
for num in range(1,11):
    address = 'human_beings/pic' + str(num).zfill(2) + '.jpg'
    print(address)
    image = cv2.imread(address, 1)
    fourierTransform = numpy.fft.fft2(image)
    amplitude = numpy.absolute(fourierTransform) * 0.5
    phase = numpy.angle(fourierTransform) * 0.8
    imageModified = numpy.ndarray.astype(numpy.absolute(numpy.fft.ifft2(amplitude*(numpy.sin(phase)*1j + numpy.cos(phase)))), numpy.uint8)
    cv2.imshow('Picture ' + str(num).zfill(2), image)
    cv2.imshow('Modified Picture ' + str(num).zfill(2), imageModified)
    cv2.waitKey()
    cv2.destroyAllWindows()