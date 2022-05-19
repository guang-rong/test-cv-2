import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def findPen(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    minimum = np.array([81, 54, 117])
    maximum = np.array([116, 176, 186])

    mask = cv2.inRange(hsv, minimum, maximum)
    result = cv2.bitwise_and(img, img, mask=mask)
    findContour(mask)

    cv2.imshow('result', result)

def findContour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        cv2.drawContours(img_contours, cnt, -1, (255, 0, 0), 4)
        area = cv2.contourArea(cnt)  # 輪廓內面積計算
        if area > 500:
            peri = cv2.arcLength(cnt, True)  # 輪廓邊長計算
            vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)  # 找輪廓頂點
            x, y, w, h = cv2.boundingRect(vertices)

# 攝像頭
while True:
    ret, frame = cap.read()
    if ret:
        img_contour = frame.copy()
        cv2.imshow('video', frame)
        findPen(frame)
        cv2.imshow('contour', img_contours)
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        break