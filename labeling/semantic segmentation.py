import os
import shutil
import random
from PIL import Image
import cv2
import numpy as np

def draw_mask(img,mask,out):
    image=cv2.imread(img)
    label=cv2.imread(mask,0)
    h,w=label.shape
    for i in range(h):
        for j in range(w):
            if label[j][i]>0:
                image[j][i]=[0,0,125]
    cv2.imwrite(out,image)

draw_mask("E:\\research/dissertation\\image\\section_2\\066_29.png","E:\\research\\dissertation\\image\\section_2\\066_29_mask.png","E:\\research/dissertation\\image\\section_2\\066_29_added.png")



def random_sample(src_path, dst_path):
    # 从样本中随机抽取部分作为train和test,并移动到指定文件
    src_img_path = "D:\AerialGoaf/refine2/256x256/train"
    src_path = "D:\AerialGoaf/refine2/256x256/trainannot"
    dst_img_path = "D:\AerialGoaf/refine2/256x256/val"
    dst_path = "D:\AerialGoaf/refine2/256x256/valannot"
    # index=np.random.random_integers(3200,size=(200,))
    files = os.listdir("D:\AerialGoaf/refine2/256x256/trainannot")
    files = random.sample(files, 200)
    for i in files:
        src_img = os.path.join(src_img_path, i)
        src_mask = os.path.join(src_path, i)
        dst_img = os.path.join(dst_img_path, i)
        dst_mask = os.path.join(dst_path, i)
        shutil.move(src_img, dst_img)
        shutil.move(src_mask, dst_mask)