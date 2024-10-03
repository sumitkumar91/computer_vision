import cv2
image = cv2.imread("wall with hole.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image[50:70, 150:170] =[144,144,142]
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cv2.imwrite("output.jpg", image)