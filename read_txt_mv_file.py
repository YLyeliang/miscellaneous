import os
import shutil

# 读取txt文件
file = 'D:/data/stitch/crop/ImageSets/Main/test.txt'
img_path = "/data/crop/VOC2007/JPEGImages"
files=[]
imgs=[]
with open(file, 'r') as f:
    while True:
        line = f.readline()
        line = line[:-1]
        files.append(line+'.jpg')
        if not line:
            break
        src = os.path.join(img_path, line) + ".jpg"
        imgs.append(src)
# path = '/data2/yeliang/data/leakage_test'
# # files= os.listdir(path)
# imgs = [os.path.join(path,i) for i in files]

debug=1

def read_txt_cp_file():
    file = 'D:/data/stitch/crop/ImageSets/Main/test.txt'
    img_path = "D:/data/visualization_leakageDataset/crop"
    dst_path = "D:/data/visualization_leakageDataset/crop/test_gt"
    with open(file, 'r') as f:
        while True:
            line = f.readline()
            line = line[:-1]
            if not line:
                break
            src = os.path.join(img_path, line) + ".jpg"
            dst = os.path.join(dst_path, line) + ".jpg"
            shutil.copy(src, dst)