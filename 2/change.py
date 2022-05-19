import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img_name.jpg')
img = cv2.resize(img, (0, 0), fx=2, fy=2)

kernal_dilate = np.ones((7, 7), np.uint8)
kernal_erode = np.ones((7, 7), np.uint8)

# 90度旋轉
rows, cols, _ = img.shape
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
dst = cv2.warpAffine(img, M, (cols, rows))

# 平移
M = np.float32([[1, 0, 60], [0, 1, 80]])
im = cv2.warpAffine(img, M, (rows, cols))

# 圖片灰階化
gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

# 高斯模糊
gaussi = cv2.GaussianBlur(img, (15, 15), 5)

# 直方圖
cv2.destroyAllWindows()
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

# 邊緣擷取
canny = cv2.Canny(img, 100, 250)

# 線條加粗(膨脹)
dilate = cv2.dilate(canny, kernal_dilate, iterations=1)

# 線條變細(侵蝕)
erode = cv2.erode(dilate, kernal_dilate, iterations=1)

cv2.imshow('img', img)
cv2.imshow('det', dst)
cv2.imshow('image', im)
cv2.imshow('gray', gray)
cv2.imshow('gaussi', gaussi)
cv2.imshow('canny', canny)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)

cv2.waitKey(0)