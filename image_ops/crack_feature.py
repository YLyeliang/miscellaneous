import os
import cv2
from mtcv import findContours, minAreaRect
import math
import numpy as np

def eucliDist(A,B):
    return math.sqrt(sum([(a - b)**2 for (a,b) in zip(A,B)]))

def crack_length(skeletons):
    length = []
    for skeleton in skeletons:
        num = skeleton.shape[0]
        length.append(num)
    return length


def crack_width(skeletons, contours, q=10):
    width=[]
    for i in range(len(skeletons)):
        skeleton = skeletons[i]
        contour = contours[i]
        num = skeletons[i].shape[0]
        segment = num // q
        segments = [segment * q_length for q_length in range(q)]
        accumulator=0
        distance=[]
        for seg in segments:
            ske = skeleton[seg:seg + segment]
            len_ske = len(ske)
            if len_ske > 2:
                sx, sy = ske[0][0]
                ex, ey = ske[-1][0]
                mx, my = ske[len_ske // 2][0]
                # y= ax + b line between start dot and end dot
                a = (ey - sy) / (ex - sx)
                # y=kx + c vertical line by the mid dot
                k = -1 / a
                c = my - k * mx
                # calculate distance
                intersect_dot = []
                for dot in contour:
                    x, y = dot[0]
                    dis = abs((k * x - y + c))
                    if dis < 1:
                        intersect_dot.append([x, y])
                if len(intersect_dot) > 2:
                    tmp_dot=[]
                    dist = [eucliDist(dot,(mx,my)) for dot in intersect_dot]
                    index = np.argsort(dist)
                    if intersect_dot[index[-1]][0]-intersect_dot[index[-2]][0]<=1 and intersect_dot[index[-1]][1]-intersect_dot[index[-2]][1]<=1:
                        tmp_dot.append(intersect_dot[index[-1]])
                        tmp_dot.append(intersect_dot[index[-3]])
                    else:
                        tmp_dot.append(intersect_dot[index[-1]])
                        tmp_dot.append(intersect_dot[index[-2]])
                    intersect_dot=tmp_dot
            if len(intersect_dot)==2:
                dist=eucliDist(intersect_dot[0],intersect_dot[1])
                if dist>1.5:
                    accumulator+=1
                    distance.append(dist)
        if not accumulator==0:
            mean_dist=sum(distance)/accumulator
        else:
            mean_dist=0
        width.append(mean_dist)
    return width


root = "E:/research\dissertation\image\section_5"
img_name = "072.png"
skeleton_name = "072_skeleton.png"

# read image and skeleton
image = cv2.imread(os.path.join(root, img_name))
skeleton = cv2.imread(os.path.join(root, skeleton_name), 0)
mask = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# find contours
cnt_img, contours_img, hierachy = findContours(mask)
cnt_ske, contours_ske, _ = findContours(skeleton)
# remove very small contours
contours_tmp=[]
for contour in contours_img:
    if contour.shape[0]>20:
        contours_tmp.append(contour)
contours_img=contours_tmp

# crack width
width=crack_width(contours_ske, contours_img)

# calculate rect area and contour area.
rect,cnt_area = minAreaRect(contours_img)
box_keep=[]
for i in rect:
    box = cv2.boxPoints(i)
    box = np.int0(box)
    box_keep.append(box)
rect_area=[]
for i in box_keep:
    area_=cv2.contourArea(i)
    rect_area.append(area_)

# crack length
length = crack_length(contours_img)

# ratio of area.
rect_ratio=[a/b for a,b in zip(cnt_area,rect_area)]

for i in range(len(contours_ske)):
    print("{}th crack".format(i))
    print("length: {}, width: {}, rect_area: {}, cnt_area: {}, rect_ratio: {}".format(length[i],width[i],rect_area[i],cnt_area[i],rect_ratio[i]))

for i, cnt in enumerate(contours_img):
    dot=tuple(cnt[0][0]-15)
    cv2.putText(image,str(i+1),dot,cv2.FONT_HERSHEY_COMPLEX,1.2,(255,255,255),2)
# cv2.drawContours(image, contours_img, -1, color=(255, 0, 0), thickness=1)
cv2.drawContours(image,box_keep,-1,color=(0,255,0),thickness=1)
cv2.imwrite(os.path.join(root,img_name[:4]+'_feat.png'),image)
cv2.imshow("contours", image)
# cv2.imshow("rect",rect)
cv2.waitKey()
