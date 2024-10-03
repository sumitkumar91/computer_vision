import cv2
import play

img = cv2.imread("panda.jpg")
print(img.shape)
print(img)
bgr = img[150,46]
print(bgr[0], bgr[1], bgr[2])
img = cv2.resize(img, (450, 450))
print(img.shape)
print(img)
cv2.imwrite("output.jpg", img)
play.set_backdrop("blue")
play.new_image("panda.jpg")
play.start_program()