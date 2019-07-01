import os
import shutil

# 读取txt文件
file='D:/data/No_Pinjie/ImageSets/Main/val.txt'
img_path="D:/data/visualization_leakageDataset"
dst_path="D:/tmp/gt"
with open(file,'r') as f:
    while True:
        line=f.readline()
        line=line[:-1]
        if not line:
            break
        src=os.path.join(img_path,line)+".jpg"
        dst=os.path.join(dst_path,line)+".jpg"
        shutil.copy(src,dst)
