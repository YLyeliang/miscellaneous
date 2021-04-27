import os
import shutil
import random

# 给定图片目录和文本目录，将文件记录到文本并输出到文本目录
# 在过程中进行随机采样

img_path="D:\zmhj_photo\det_img\crop_new\JPEGImages"
txt_path="D:\zmhj_photo\det_img\crop_new\ImageSets/Main"

def write_txt(img_path,txt_path):
    img_files=os.listdir(img_path)
    number=len(img_files)
    train_files=img_files
    test_files=random.sample(img_files,round(number/4))
    for i in test_files:
        train_files.remove(i)
    train_files = [i[:-4] for i in train_files]
    test_files = [i[:-4] for i in test_files]
    if not os.path.exists(txt_path):
        os.makedirs(txt_path)
    with open(os.path.join(txt_path, "trainval.txt"),'w') as f:
        for train in train_files:
            f.write(train+'\n')

    with open(os.path.join(txt_path,"test.txt"),'w') as f:
        for test in test_files:
            f.write(test+'\n')

    debug=1

write_txt(img_path,txt_path)