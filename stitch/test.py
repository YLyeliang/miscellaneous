import cv2
import os

img="D:/stitch_test/5/5_Line17_up_20190411032435_1_34km+774.9m_forward.jpg"
cv2.namedWindow("img",cv2.WINDOW_NORMAL)
img=cv2.imread(img)
pt1=(1583,57)
pt2=(1710,556)
cv2.rectangle(img,pt1,pt2,color=(0,0,255),thickness=2)
cv2.imshow("img",img)
cv2.waitKey()