import cv2

img = cv2.imread("baloon bg.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

rectangle = cv2.rectangle(img, (30, 500), (630, 1030), (255, 255, 255), 8)
cv2.putText(img, "Happy", (50,675), cv2.FONT_HERSHEY_TRIPLEX, 3, (255, 255, 255), 2, (cv2.LINE_AA))
cv2.putText(img, "Birthday", (120, 800), cv2.FONT_HERSHEY_TRIPLEX, 3, (255, 255, 255), 2, (cv2.LINE_AA))
cv2.putText(img, "to you", (160, 965), cv2.FONT_HERSHEY_TRIPLEX, 3, (255, 255, 255), 2, (cv2.LINE_AA))

out = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
out = cv2.imwrite("output.jpg", out)