import numpy as np
import cv2
from matplotlib import pyplot as plt

def co_occurrence(img):
  co_oc = np.zeros((256, 256))
  for i in range(0, len(img)):
    for j in range(0, len(img[i])):
      if i != 0:
        co_oc[img[i,j], img[i-1,j]] += 1
      if j != 0:
        co_oc[img[i,j], img[i,j-1]] += 1
      if i != len(img)-1:
        co_oc[img[i,j], img[i+1,j]] += 1
      if j != len(img[0])-1:
        co_oc[img[i,j], img[i,j+1]] += 1
  return co_oc

I = cv2.imread('dinosaur.jpg')
I = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
S = [I]
co_S = [co_occurrence(I)]
total_co_S = [co_S[0].sum()]
R = [I-S[0]]
total_co_S2 = [R[0].sum()/(256*256)]

for n in range(1, 31):
  S.append(cv2.medianBlur(S[n-1],3))
  co_S.append(co_occurrence(S[n]))
  total_co_S.append(co_S[n].sum())
  R.append(I - S[n])
  total_co_S2.append(R[n-1].sum()/(256*256))
  print("Image {} calculated!".format(n))

co_I = co_occurrence(I)


plt.plot(total_co_S2)
plt.show()

# for n in range(0, 31):
cv2.imshow('Image',S[30])
cv2.imshow('Residual Image',R[30])
cv2.waitKey(0)