import os
from mtcv.image import resize
import cv2

# img_path ="D:/zmhj_photo/raw_det"
# img_out = "D:/zmhj_photo/raw_det/1125x768"
# for i in os.listdir(img_path):
#     if not "JPG" in i:
#         continue
#     img = os.path.join(img_path,i)
#     img2 = resize(img,dsize=(1125,768))
#     cv2.imwrite(os.path.join(img_out,i),img2)

#bgr to gray
def rgb_data_to_gray(rgb_path,gray_path):
    rgb_data=['train','val','test']
    rgb=[os.path.join(rgb_path,dir) for dir in rgb_data]
    gray=[os.path.join(gray_path,dir) for dir in rgb_data]
    for i in range(3):
        rgb_files=os.listdir(rgb[i])
        if not os.path.exists(gray[i]):
            os.makedirs(gray[i])
        for file in rgb_files:
            img = cv2.imread(os.path.join(rgb[i],file),0)
            cv2.imwrite(os.path.join(gray[i],file),img)

src="D:\\data\\detail"
dst="D:\\data\\gray"
rgb_data_to_gray(src,dst)