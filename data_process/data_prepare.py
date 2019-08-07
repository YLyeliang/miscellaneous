import os
import shutil
import random

def mv_jpg_xml():
    path = "D:/data/20190711反馈2/20190711反馈2\Camera2_no"
    xml_out = "D:\data/train_data/20190730/Annotations"
    jpg_out = "D:\data/train_data/20190730/JPEGImages"
    files_tmp = os.listdir(path)
    files = []
    for i in files_tmp:
        if 'xml' in i:
            files += [i]
    files.sort()
    postfix = 'jpg'
    for file in files:
        if not os.path.exists(xml_out):
            os.mkdir(xml_out)
        if not os.path.exists(jpg_out):
            os.mkdir(jpg_out)
        file_abs = os.path.join(path, file)
        file_out = os.path.join(xml_out, file)
        img_abs = os.path.join(path, file[:-3] + postfix)
        img_out = os.path.join(jpg_out, file[:-3] + postfix)
        shutil.copy(file_abs, file_out)
        shutil.copy(img_abs, img_out)

def write_txt_random_sample(img_path,txt_path):
    # 给定图片目录和文本目录，将文件记录到文本并输出到文本目录
    # 在过程中进行随机采样
    img_files=os.listdir(img_path)
    number=len(img_files)
    train_files=img_files
    # decide how many images used to test.
    test_files=random.sample(img_files,45)
    for i in test_files:
        train_files.remove(i)
    train_files = [i[:-4] for i in train_files]
    test_files = [i[:-4] for i in test_files]
    train_files.sort()
    test_files.sort()
    if not os.path.exists(txt_path):
        if not os.path.exists(txt_path[:-4]):
            os.mkdir(txt_path[:-4])
        os.mkdir(txt_path)
    with open(os.path.join(txt_path, "trainval.txt"),'w') as f:
        for train in train_files:
            f.write(train+'\n')

    with open(os.path.join(txt_path,"test.txt"),'w') as f:
        for test in test_files:
            f.write(test+'\n')

img_path="D:/data/train_data/20190730/JPEGImages"
txt_path="D:/data/train_data/20190730/ImageSets/Main"
write_txt_random_sample(img_path,txt_path)
# mv_jpg_xml()