import cv2
import numpy as np
from skimage import io
from scipy import ndimage

img = cv2.imread('img_name.jpg')
img = cv2.resize(img, (0, 0), fx=2, fy=2)

cv2.imshow('img', img)

cv2.waitKey(0)