import cv2
p=cv2.imread('4.jpg')
p=cv2.cvtColor(p,cv2.COLOR_RGB2GRAY)
p=cv2.resize(p,(690,390))
for i in range(p.shape[0]):
    for j in range(p.shape[1]):
        if p[i,j]>40:
            p[i,j]=255

cv2.imshow('X4',p)
cv2.waitKey()