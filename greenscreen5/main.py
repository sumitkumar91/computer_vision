import cv2

FACE_CASCADE = cv2.CascadeClassifier("face.xml")
print(FACE_CASCADE)

img = cv2.imread("groupphoto.jpg")
img = cv2.resize(img, (1000, 500))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

faces = FACE_CASCADE.detectMultiScale(gray, 1.1, 5)

for (x,y,w,h) in faces:
  cv2.rectangle(img, (x,y), (x+w, h+y), (255,0,0), 3)

print(faces)
cv2.imwrite("output.jpg", img)