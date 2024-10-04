import cv2

ingimage = cv2.imread("bg.jpeg")
ingimage = cv2.cvtColor(ingimage, cv2.COLOR_BGR2RGB)

img = cv2.imread("cloak.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img = cv2.resize(img, (325, 600))
ingimage = cv2.resize(ingimage, (325, 600))

h = ingimage.shape[0]
w = ingimage.shape[1]

h1 = img.shape[0]
w1 = img.shape[1]

for i in range(h1):
  for j in range(w1):
    red = img[i, j, 0]
    green = img[i, j, 1]
    blue = img[i, j, 2]
    if not (red < 60 and green < 185 and blue > 80):
      ingimage[i, j] = img[i, j]

ingimage = cv2.cvtColor(ingimage, cv2.COLOR_RGB2BGR)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imwrite("output.jpg", ingimage)
