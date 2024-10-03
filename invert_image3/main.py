import cv2
import numpy

img = numpy.zeros((100, 100))
print(img.shape)
print(img)
img =numpy.uint8(img)
print(img.shape)
print(img)
img[: , :] = 125
cv2.imwrite("output.jpg", img)