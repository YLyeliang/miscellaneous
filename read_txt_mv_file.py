import os
import shutil

# 读取txt文件
file='D:/data/No_Pinjie/ImageSets/Main/trainval.txt'
img_path="D:/data/No_Pinjie/JPEGImages"
dst_path="D:/tmp/No_pinjie_src"
with open(file,'r') as f:
    while True:
        line=f.readline()
        line=line[:-1]
        if not line:
            break
        src=os.path.join(img_path,line)+".jpg"
        dst=os.path.join(dst_path,line)+".jpg"
        shutil.copy(src,dst)
