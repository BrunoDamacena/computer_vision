import cv2
from matplotlib import pyplot
import numpy

img = cv2.imread('image.png', 0)

floatImg = numpy.float32(img)

discreteFourierTransform = cv2.dft(floatImg, flags = cv2.DFT_COMPLEX_OUTPUT)
dftShift = numpy.fft.fftshift(discreteFourierTransform)


# fourierTransform = numpy.fft.fft2(img)
# shiftedTransform = numpy.fft.fftshift(fourierTransform)
# magnitudeSpectrum = 20*numpy.log(numpy.abs(shiftedTransform))

# img_back = cv2.idft(f_ishift)
# img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

# pyplot.imshow(magnitudeSpectrum, cmap = 'gray')
# pyplot.xticks([]), pyplot.yticks([])
# pyplot.show()