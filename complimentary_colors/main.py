import cv2

img = cv2.imread("flowers.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

c = img.copy()
c = 255 - img

img = cv2.cvtColor(c, cv2.COLOR_RGB2BGR)
cv2.imwrite("output.jpg", img)

img = cv2.imread("man.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

c = img.copy()
c = 255 - img

img = cv2.cvtColor(c, cv2.COLOR_RGB2BGR)
cv2.imwrite("output.jpg", img)