import cv2

img = cv2.imread("para.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img1 = cv2.imread("pt logo.png")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

h = img1.shape[0]
w = img1.shape[1]

img[0:h, 0:w] = img1

img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2BGR)
cv2.imwrite("output.jpg", img)