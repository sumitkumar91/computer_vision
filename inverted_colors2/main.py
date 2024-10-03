import cv2

img = cv2.imread("eyes.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(img.shape)
print(img)

cv2.circle(img, (155, 292), 103, (255,0,0), 2)
cv2.circle(img, (434, 292), 103, (255,0,0), 2)

img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imwrite("output.jpg", img)