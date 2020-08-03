import cv2, os, time

camera = cv2.VideoCapture(0)

while True:
  _, frame = camera.read()
  img = cv2.resize(frame, (320, 240))
  cv2.imwrite('tmp.jpg', img)
  os.rename('tmp.jpg', 'live.jpg')
  time.sleep(0.3)