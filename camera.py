import cv2

camera = cv2.VideoCapture(0)

_, frame = camera.read()

cv2.imwrite("test-opencv.jpg", frame)
