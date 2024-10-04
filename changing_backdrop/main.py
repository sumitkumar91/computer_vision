import cv2
img = cv2.imread("img.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img1 = cv2.imread("New background.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
print(img1.shape, img.shape)
print(img1)
h = img.shape[0]
w = img.shape[1]
img1 = cv2.resize(img1, (300, 300))
for i in range(h):
  for j in range(w):
    pixel = img[i, j]
    if not(pixel[0]>=205 and pixel[1]>= 245 and pixel[2]>=125):
      img1[i,j]= img[i,j]

img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2BGR)
cv2.imwrite("output.jpg", img1)