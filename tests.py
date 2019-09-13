import numpy as np
# from PIL import Image
import matplotlib.pyplot as plt
import cv2
import collections
import time
import torch
from mtcv import histEqualize
import os
import logging


x=torch.arange(0,8).view(2,4)
y=torch.arange(100,112).view(3,4)
c=x[None,:,:]+y[:,None,:]
d=c.view(-1,4)


ratios=[0.5,1,2]
scales=[8,16,32]
scale =torch.Tensor(scales)
ratio=torch.Tensor(ratios)
w=4
r=ratio[:,None]
s=scale[None,:]
res=w*r*s
res_=res.view(-1)
print(res)


arr=np.arange(0,20).reshape(4,5)
for i in arr:
    print(i)

a=[3,7,13,20,30,40]
b=[1,3,4]
c=[a[i] for i in b]

a=list(range(10,0,-1))
print(a)

def yiled_demo(a,b):
    for i in range(len(a)):
        c=a[i]*b[i]
        d=a[i]*b[i]*c
        yield c,d

a=[1,2,3,4,5]
b=[6,7,8,9,10]
g=yiled_demo(a,b)
for i in range(len(a)):
    print(g.__next__())


# 图像输出质量决定
img=cv2.imread('D:\stitch_test\line17_stitch/Line17_up_20190411032624_128_33km+462.6m_forward.jpg')
cv2.imwrite("src_66.jpg",img,[int(cv2.IMWRITE_JPEG_QUALITY),40])

concat_width=500
img_h=4000

rgb = np.zeros((img_h,concat_width,3), dtype=np.uint8)

cv2.putText(rgb,"#224",(20,200),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,5,color=(0,0,255),thickness=3)
# cv2.imwrite("rgb.jpg",rgb)
cv2.namedWindow("img",cv2.WINDOW_NORMAL)
cv2.imshow("img",rgb)
cv2.waitKey()


a=['1','2','3','4','5']
b=['a','b','c','d','e']
a_arr=np.array(a)
b_arr=np.array(b)
c=np.stack((a_arr,b_arr))


img="1_Line17_up_20190411033847_911_25km+381.3m_forward.jpg"
img_arr=img.split('_')
new="_".join(img_arr[1:])


img=cv2.imread(img)
img=histEqualize(img,space='rgb',clipLimit=10)
cv2.namedWindow("img",cv2.WINDOW_NORMAL)
cv2.imshow("img",img)
cv2.waitKey()




# def show_CLAHE(path):
#     path=




file=os.listdir("D:/tmp/test")
file.sort(key=lambda x:x[:-4])

# a=max(None,None)



a=[1,1,1,2,2,3,4,5,1,2,7,5,3,2]
i=0
while True:
    j=i+1
    while True:
        if a[i]==a[j]:
            del a[j]
        else:
            j+=1
        if j >= len(a):
            break
    i+=1
    if i == len(a)-1:
        break
print(a)





for i in range(0):
    print(0)
a=[1,2,3]
b=[4,5,6]
c=a+b



x=torch.arange(0,8).view(2,4)
y=torch.arange(100,112).view(3,4)
c=x[None,:,:]+y[:,None,:]
d=c.view(-1,4)


ratios=[0.5,1,2]
scales=[8,16,32]
scale =torch.Tensor(scales)
ratio=torch.Tensor(ratios)
w=4
r=ratio[:,None]
s=scale[None,:]
res=w*r*s
res_=res.view(-1)
print(res)



class A(object):
    def __init__(self,name):
        self._name=name
        self._module_dict=dict()

    @property
    def name(self):
        return self._name

    @property
    def module_dict(self):
        return self._module_dict

    def _register(self,module_class):
        self._module_dict["wang"]=module_class


    def register(self,cls):
        self._register(cls)
        return cls

cls_A=A('loss')

@cls_A.register
class B(object):
    def __init__(self):
        print('haha')

    @property
    def hehe(self):
        return self.b

cls_c = cls_A.module_dict['wang']
d=cls_c.hehe

print(cls_c)

debug=1





# cap=cv2.VideoCapture(0)
# while True:
#     ret,frame=cap.read()
#     cv2.imshow("frame",frame)
#     if cv2.waitKey(1) &0xff== ord('q'):
#         break

