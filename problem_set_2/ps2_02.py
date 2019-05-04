import cv2
import numpy as np
from skimage.exposure import rescale_intensity

def convolve(image, kernel):
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]
    pad = (kW - 1) // 2
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype="float32")
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
            k = (roi * kernel).sum()
            output[y - pad, x - pad] = k
    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")
    return output

image = cv2.imread('edge_detection2.png', 0)

kernel = np.array((
    [-1,1,2],
    [2,0,-2],
    [-2,-1,1]
), dtype = "int")

edgesImage = convolve(image, kernel)
cv2.imshow("Original Image", image)
cv2.imshow("Edges", edgesImage)
cv2.waitKey()

cv2.imwrite('equalized.png', edgesImage)