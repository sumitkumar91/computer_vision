import cv2
img=cv2.imread("lionbw.jpg",cv2.IMREAD_GRAYSCALE)
print(img.shape)
print(img)
h=img.shape[0]
w=img.shape[1]
for i in range(h):
  for j in range(w):
    if img[i,j]<120:
      img[i,j]=255
    elif img[i,j]>=120:
      img[i,j]=0

cv2.imwrite("output.jpg",img)