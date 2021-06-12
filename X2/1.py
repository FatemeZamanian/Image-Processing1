import cv2
import numpy as np
x = cv2.imread('1.jpg')
x = cv2.cvtColor(x,cv2.COLOR_RGB2GRAY)
x = 255-x
x=cv2.resize(x,(300,300))
y = cv2.imread('2.jpg')
y = cv2.cvtColor(y,cv2.COLOR_RGB2GRAY)
y = 255-y
y=cv2.resize(y,(300,300))
xy=np.concatenate((x,y))
cv2.imshow('x2', xy)
cv2.waitKey()