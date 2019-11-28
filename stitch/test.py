import cv2
import os

img="D:/lenna.jpg"
cv2.namedWindow("img",cv2.WINDOW_NORMAL)
img=cv2.imread(img)
pt1=(183,57)
pt2=(510,556)
cv2.rectangle(img,pt1,pt2,color=(0,0,255),thickness=2)
cv2.imshow("img",img)
cv2.waitKey()