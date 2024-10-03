import cv2
img = cv2.imread("rgb.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img.shape)
print(img)
img[:,:,0] = 0
img[:,:,1] = 0
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imwrite("output.jpg", img)