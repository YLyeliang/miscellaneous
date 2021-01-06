import cv2
import numpy as np

# im = cv2.imread('00016_38.png', cv2.IMREAD_GRAYSCALE)
# thresh, im = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# cv2.imshow('binary.png', im)  # 控制背景为黑色
# dst = im.copy()
#
# num_erode = 0
#
# while (True):
#     if np.sum(dst) == 0:
#         break
#     kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
#     dst = cv2.erode(dst, kernel)
#     num_erode = num_erode + 1
#
# skeleton = np.zeros(dst.shape, np.uint8)
#
# for x in range(num_erode):
#     kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
#     dst = cv2.erode(im, kernel, None, None, x)
#     open_dst = cv2.morphologyEx(dst, cv2.MORPH_OPEN, kernel)
#     result = dst - open_dst
#     skeleton = skeleton + result
#     cv2.waitKey(1000)
#
# cv2.imshow('result', skeleton)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import os
import numpy as np
import cv2
import sys

im = cv2.imread('00016_38.png', cv2.IMREAD_GRAYSCALE)

ret, im = cv2.threshold(im, 30, 255, cv2.THRESH_BINARY)
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

skel = np.zeros(im.shape, np.uint8)
erode = np.zeros(im.shape, np.uint8)
temp = np.zeros(im.shape, np.uint8)

i = 0
while True:
    cv2.imshow('im %d' % (i), im)
    erode = cv2.erode(im, element)
    temp = cv2.dilate(erode, element)

    # 消失的像素是skeleton的一部分
    temp = cv2.subtract(im, temp)
    cv2.imshow('skeleton part %d' % (i,), temp)
    skel = cv2.bitwise_or(skel, temp)
    im = erode.copy()

    if cv2.countNonZero(im) == 0:
        cv2.destroyAllWindows()
        break
    i += 1
cv2.imshow('Skeleton', skel)
element = cv2.getStructuringElement(cv2.MORPH_OPEN, (2, 2))
erode = cv2.erode(skel, element)
temp = cv2.dilate(erode, element)
cv2.imshow('erode', temp)
cv2.waitKey()
