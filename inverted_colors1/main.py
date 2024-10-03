import cv2
img = cv2.imread("img.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img.shape)
print(img)
cv2.rectangle(img, (51,41), (293,288), (255,0,0), 2)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imwrite("output.jpg", img)