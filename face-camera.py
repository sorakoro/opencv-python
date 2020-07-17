import cv2
import os
from datetime import datetime
from time import sleep

CASCADE_DIR = os.environ["HOME"] + "/.pyenv/versions/3.6.0/usr/local/share/OpenCV/haarcascades"
CASCADE_FILE = CASCADE_DIR + "/haarcascade_frontalface_alt.xml"

MIN_SIZE = (150, 150)

cascade = cv2.CascadeClassifier(CASCADE_FILE)

camera = cv2.VideoCapture(0)

try:
  while True:
    _, img = camera.read()

    igray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(igray, minSize=MIN_SIZE)

    if len(faces) == 0:
      continue

    for (x, y, w, h) in faces:
      color = (255, 0, 0)
      cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness = 8)

      s = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
      fname = "face" + s + ".jpg"

      cv2.imwrite(fname, img)
      print("顔を認識しました")
      sleep(3)

except KeyboardInterrupt:
  print("ok")
