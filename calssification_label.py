import numpy as np
import os, shutil
import cv2

# stages=(3,4,6,3)
# stage_blocks=stages[:4]
# for i,block in enumerate(stage_blocks):
#     print(64*2**i,i,block)

debug = 1

path = "D:/images/ch05_20190526132103"
outpath = ("D:\images/blue", "D:\images/white", "D:\images/door", "D:\images/no_cover", "D:\images/normal")



def move_file(path):
    for imgfile in os.listdir(path):
        srcfile=os.path.join(path, imgfile)
        img = cv2.imread(srcfile)
        cv2.namedWindow("img",cv2.WINDOW_NORMAL)
        cv2.imshow("img", img)
        key = cv2.waitKey() & 0xff
        if key == ord('q'):  # 蓝色洗衣液
            blue_path=os.path.join(path,"blue")
            if not os.path.exists(blue_path):
                os.mkdir(blue_path)
            dstfile = os.path.join(blue_path, imgfile)
            shutil.move(srcfile, dstfile)
        elif key == ord('w'):   #白色洗衣液
            white_path=os.path.join(path,"white")
            if not os.path.exists(white_path):
                os.mkdir(white_path)
            dstfile = os.path.join(white_path,imgfile)
            shutil.move(srcfile,dstfile)
        elif key ==ord('e'):    #开门
            door_path=os.path.join(path,"door")
            if not os.path.exists(door_path):
                os.mkdir(door_path)
            dstfile = os.path.join(door_path,imgfile)
            shutil.move(srcfile,dstfile)
        elif key==ord('r'):     #无盖
            no_cover_path=os.path.join(path,"no_cover")
            if not os.path.exists(no_cover_path):
                os.mkdir(no_cover_path)
            dstfile =os.path.join(no_cover_path,imgfile)
            shutil.move(srcfile,dstfile)
        elif key == ord('t'):   #正常
            normal_path=os.path.join(path,"normal")
            if not os.path.exists(normal_path):
                os.mkdir(normal_path)
            dstfile = os.path.join(normal_path,imgfile)
            shutil.move(srcfile,dstfile)

move_file(path)
