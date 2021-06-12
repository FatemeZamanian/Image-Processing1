import cv2,array
z=cv2.imread('3.jpg')
z=cv2.resize(z,(428,560))
(h,w)=z.shape[:2]
center=(w/2,h/2)
zz=cv2.getRotationMatrix2D((center),180,1.0)
zzz=cv2.warpAffine(z,zz,(w,h))
cv2.imshow('X3',zzz)
cv2.waitKey()