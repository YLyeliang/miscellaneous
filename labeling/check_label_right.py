import os
import shutil
import cv2 as cv

path="D:/data/visualization_leakageDataset"
out="uncertain"

def check_img(path,out):
    cv.namedWindow("image",cv.WINDOW_NORMAL|cv.WINDOW_KEEPRATIO)
    files = os.listdir(path)
    files.sort(key=lambda x:x[:-4])
    for file in files:
        img_path= os.path.join(path,file)
        img =cv.imread(img_path)
        cv.imshow("image",img)
        key = cv.waitKey() &0xff
        if key == ord("g"):
            out_path=os.path.join(path,out)
            if not os.path.exists(out_path):
                os.mkdir(out_path)
            dst_path=os.path.join(out_path,file)
            shutil.copy(img_path,dst_path)

check_img(path,out)
