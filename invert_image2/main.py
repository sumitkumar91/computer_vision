import cv2

img = cv2.imread("black 100x100.jpg", cv2.IMREAD_GRAYSCALE)
print(img.shape)
print(img)
print(img[2,2])
img[2,2] = 255
img[2:30, 2:180] = 255
print(img[2,2])
cv2.imwrite("output.jpg", img)