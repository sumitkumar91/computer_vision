import cv2

count = 0
out = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc("M", "J", "P", "G"), 10, (600, 900))

face_classifier = cv2.CascadeClassifier("face.xml")
print(face_classifier)

framecount = 0
capture = cv2.VideoCapture("video.mp4")
totalframes = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
frameheight = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
framewidth = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
framefps = capture.get(cv2.CAP_PROP_FPS)

print(totalframes)
print(frameheight)
print(framewidth)
print(framefps)

while (capture.isOpened()):
  framecount += 1
  status, frame = capture.read()

  if status:
    count += 1
    fg_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_classifier.detectMultiScale(frame, 1.8, 4)

    for (w, h, x, y) in faces:
      cv2.rectangle(fg_img, (x,y), (x+w, y+h), (255,0,0), 3)
    print(faces)
    fg_img = cv2.resize(fg_img, (600, 800))
    fg_img = cv2.cvtColor(fg_img, cv2.COLOR_RGB2BGR)
    cv2.imwrite("upload" +str(count) +".jpg", fg_img)
    out.write(fg_img)
  else:
    print("breaking out of loop")
    break

cv2.destroyAllWindows()
print("completed")
capture.release()
