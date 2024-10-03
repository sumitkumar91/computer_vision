import cv2
import numpy

img = numpy.zeros((100, 100, 3))

print(img.shape)
print(img)

img = numpy.uint8(img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(img.shape)
print(img)

img[:, :, 0] = 255
img[:, :, 1] = 0
img[:, :, 2] = 0

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imwrite("output.jpg", img)