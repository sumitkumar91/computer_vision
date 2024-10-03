import cv2

img = cv2.imread("fingerprint.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h = img.shape[0]
w = img.shape[1]

threshold = 10

outimg = img.copy()

for i in range(h - 1):
  for j in range(w - 1):
    cpixel = int(outimg[i,j])
    ncpixel = int(outimg[i,j+1])
    nrpixel = int(outimg[i+1,j])
    if abs(cpixel - ncpixel) >50 or abs(cpixel - nrpixel) >50:
      outimg[i,j] = 255
    else:
      outimg[i,j] = 0

output = cv2.cvtColor(outimg, cv2.COLOR_GRAY2BGR)
output = cv2.imwrite("fingerprint_output.jpg", outimg)
print("finished")

