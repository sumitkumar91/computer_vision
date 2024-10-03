import cv2
img = cv2.imread("img.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img.shape)
print(img)
h = img.shape[0]
w = img.shape[1]

for i in range(h):
  for j in range(w):
    pixel = img[i, j]
    if pixel[0]>=205 and pixel[1]>=245 and pixel[2]>=125:
      img[i,j] = [255,255,255]

img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imwrite("output.jpg", img)