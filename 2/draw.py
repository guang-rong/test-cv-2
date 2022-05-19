import cv2
import numpy as np

img = cv2.imread('img_name.jpg')
img = cv2.resize(img, (0, 0), fx=2, fy=2)

canvas = np.zeros((600, 600, 3), np.uint8)

# 畫線條
cv2.line(canvas, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)

# 畫方形
cv2.rectangle(canvas, (0, 0), (400, 300), (0, 0, 255), 2)  # cv2.FILLED 填滿

# 畫圓形
cv2.circle(canvas, (300, 400), 30, (255, 0, 0), 2)

# 英文投射
cv2.putText(canvas, 'HELLO', (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

cv2.imshow('canvas', canvas)

cv2.waitKey(0)