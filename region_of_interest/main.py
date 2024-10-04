import cv2
image = cv2.imread("bg1.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image[76:115, 238:311] = [144, 244, 255]
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cv2.imwrite("output.png", image)

image = cv2.imread("rcface.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image[34:102, 34:102] = [209, 30, 69]
image[197:267, 197:267] = [209, 30, 69]
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cv2.imwrite("output.png", image)