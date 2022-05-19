import cv2
import numpy as np

color = cv2.imread('color.jpg')

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