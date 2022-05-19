import cv2
import numpy as np

def a(v):
    pass

kernal_dilate = np.ones((7, 7), np.uint8)
kernal_erode = np.ones((7, 7), np.uint8)

img = cv2.imread('img_name.jpg')
img = cv2.resize(img, (0, 0), fx=2, fy=2)
img1 = cv2.imread('Winni.jpg')
img1 = cv2.resize(img1, (0, 0), fx=0.5, fy=0.5)
color = cv2.imread('color.jpg')

canvas = np.zeros((600, 600, 3), np.uint8)

# 圖片灰階化
gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

# 高斯模糊
gaussi = cv2.GaussianBlur(img, (15, 15), 5)

# 邊緣擷取
canny = cv2.Canny(img, 100, 250)

# 線條加粗(膨脹)
dilate = cv2.dilate(canny, kernal_dilate, iterations=1)

# 線條變細(侵蝕)
erode = cv2.erode(dilate, kernal_dilate, iterations=1)

# 畫線條
cv2.line(canvas, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)

# 畫方形
cv2.rectangle(canvas, (0, 0), (400, 300), (0, 0, 255), 2)  # cv2.FILLED 填滿

# 畫圓形
cv2.circle(canvas, (300, 400), 30, (255, 0, 0), 2)

# 英文投射
cv2.putText(canvas, 'HELLO', (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

# 輪廓檢測
img_contours = color.copy()
color = cv2.cvtColor(color, cv2.COLOR_BGRA2GRAY)
canny_c = cv2.Canny(color, 150, 200)

contours, hierarchy =  cv2.findContours(canny_c, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    cv2.drawContours(img_contours, cnt, -1, (255, 0, 0), 4)
    area = cv2.contourArea(cnt)   # 輪廓內面積計算
    if area > 500:
        peri = cv2.arcLength(cnt, True)    # 輪廓邊長計算
        vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)   # 找輪廓頂點
        corners = len(vertices)             # 頂點數目
        x, y, w, h = cv2.boundingRect(vertices)
        cv2.rectangle(img_contours, (x, y), (x+w, y+h), (0, 255, 0), 4)
        if corners == 3:
            cv2.putText(img_contours, 'triangle', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif corners == 4:
            cv2.putText(img_contours, 'rectangle', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif corners == 5:
            cv2.putText(img_contours, 'pentagon', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif corners >= 6:
            cv2.putText(img_contours, 'circle', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('color', color)
cv2.imshow('canny_c', canny_c)
cv2.imshow('img_contours', img_contours)
cv2.waitKey(0)

# cv2.imshow('img', img)
# cv2.imshow('gray', gray)
# cv2.imshow('gaussi', gaussi)
# cv2.imshow('canny', canny)
# cv2.imshow('dilate', dilate)
# cv2.imshow('erode', erode)
# cv2.imshow('canvas', canvas)