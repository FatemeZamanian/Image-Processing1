import cv2
import numpy as np

img = np.zeros((400, 400, 3), np.uint8)
flag = True
m = img.shape[0]//8
n = img.shape[1]//8

for i in range(0, img.shape[0], m):
    for j in range(0, img.shape[1], n):
        if not flag:
            img[i:i+m, j:j + n] = 255
            flag = True
        else:
            img[i:i+m, j:j+n] = 0
            flag = False
    if flag:
        flag = False
    else:
        flag = True
cv2.imshow('x1', img)
cv2.waitKey()
