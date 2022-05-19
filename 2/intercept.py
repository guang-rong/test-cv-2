import cv2
import numpy as np

img = cv2.imread('img_name.jpg')
img = cv2.resize(img, (0, 0), fx=2, fy=2)


