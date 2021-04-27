import cv2
import os
import shutil


def img_format_transform(src,dst,format='jpg',delete=False):
    src_files=os.listdir(src)
    for file in src_files:
        if '.' not in file:
            continue
        res = file.split('.')[0]+'.'+format
        img_path = os.path.join(src,file)
        dst_path = os.path.join(dst,res)
        img = cv2.imread(img_path)
        cv2.imwrite(dst_path,img)
        if delete:
            os.remove(img_path)

img_format_transform("D:\zmhj_photo\det_img\crop_new","D:\zmhj_photo\det_img\crop_new\jpg",delete=True)