import cv2
import numpy as np

def a(v):
    pass

cap = cv2.VideoCapture(0)

# HSV轉化
cv2.namedWindow('TrackBar')
cv2.resizeWindow('TrackBar', 640, 320)

cv2.createTrackbar('Hue Min', 'TrackBar', 0, 179, a)
cv2.createTrackbar('Hue Max', 'TrackBar', 179, 179, a)
cv2.createTrackbar('Sat Min', 'TrackBar', 0, 255, a)
cv2.createTrackbar('Sat Max', 'TrackBar', 255, 255, a)
cv2.createTrackbar('Val Min', 'TrackBar', 0, 255, a)
cv2.createTrackbar('Val Max', 'TrackBar', 255, 255, a)

while True:
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBar')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBar')
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBar')
    s_max = cv2.getTrackbarPos('Sat Max', 'TrackBar')
    v_min = cv2.getTrackbarPos('Val Min', 'TrackBar')
    v_max = cv2.getTrackbarPos('Val Max', 'TrackBar')

    print(h_min, h_max, s_min, s_max, v_min, v_max)

    ret, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    minimum = np.array([[h_min], [s_min], [v_min]])
    maximum = np.array([[h_max], [s_max], [v_max]])

    mask = cv2.inRange(hsv, minimum, maximum)
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('img', img)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    cv2.waitKey(1)