import cv2
count = 0
vid = cv2.VideoCapture("Aman visible.mp4")
fh = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
fw = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
fc = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fh, fw, fps,fc)
back = cv2.imread("bg.jpeg")
back = cv2.resize(back, (fw, fh))
print(back.shape)
out = cv2.VideoWriter("outputvid.avi", cv2.VideoWriter_fourcc("M", "J", "P", "G"), fps, (fw, fh))

while vid.isOpened():
  status, frame = vid.read()
  if status == True:
    count += 1
    front = cv2.resize(frame, (fw, fh))
    hfront= (front.shape[0])
    wfront= (front.shape[1])
    for i in range(hfront):
      for j in range(wfront):
        if front[i,j][0] > 90:
          if front[i,j][1] < 185:
            if front[i,j][2] < 65:
              front[i,j] = back[i,j]
              continue
    print("frame", count)
    cv2.imwrite("output" + str(count) + ".jpg", front)
    out.write(front)
  else:
    break
print("done")
vid.release()
    