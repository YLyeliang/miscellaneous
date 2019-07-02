import numpy as np
from PIL import Image
import cv2
import collections

class A(object):
    def __init__(self,str=1,**kwargs):
        self.a=str
        self.b=2

class B(A):
    def __init__(self,**kwargs):
        super(B,self).__init__(**kwargs)

        self.a=3


a=B(str="test")


# cap=cv2.VideoCapture(0)
# while True:
#     ret,frame=cap.read()
#     cv2.imshow("frame",frame)
#     if cv2.waitKey(1) &0xff== ord('q'):
#         break

a=['a','b']
b='c'
c = b in a
debug=1