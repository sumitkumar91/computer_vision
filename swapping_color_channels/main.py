import cv2

img = cv2.imread("Hands.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]

c = img.copy()

c[:, :, 0] = b
c[:, :, 1] = g
c[:, :, 2] = r

img = cv2.cvtColor(c, cv2.COLOR_RGB2BGR)
cv2.imwrite("output.jpg", img)