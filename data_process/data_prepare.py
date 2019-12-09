import os
import shutil
import random
import cv2
from mtcv.image import resize

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


def write_txt_random_sample(img_path, txt_path, test_num):
    # 给定图片目录和文本目录，将文件记录到文本并输出到文本目录
    # 在过程中进行随机采样
    img_files = os.listdir(img_path)
    number = len(img_files)
    train_files = img_files
    # decide how many images used to test.
    test_files = random.sample(img_files, test_num)
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
    with open(os.path.join(txt_path, "trainval.txt"), 'w') as f:
        for train in train_files:
            f.write(train + '\n')

    with open(os.path.join(txt_path, "test.txt"), 'w') as f:
        for test in test_files:
            f.write(test + '\n')


def remove_jpg_according_annot(annot_path, jpg_path):
    annots = os.listdir(annot_path)
    for i in annots:
        if 'xml' not in i:
            annots.remove(i)
    imgs = os.listdir(jpg_path)
    for i in annots:
        jpg = i[:-3] + 'jpg'
        imgs.remove(jpg)
    for img in imgs:
        os.remove(os.path.join(jpg_path, img))


def separate_img_label(dir, img_dir, label_dir):
    """
    Given a dir that contains images with corresponding labels, separate them into
    two dirs that contains imgs and labels, respectively.
    @param dir:
    @param img_dir:
    @param label_dir:
    @return:
    """
    dir_list = os.listdir(dir)
    if not dir_list:
        return
    else:
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)
        if not os.path.exists(label_dir):
            os.makedirs(label_dir)
        img_list = []
        label_list = []
        for i in dir_list:
            if 'xml' in i:
                label_list.append(i)
            else:
                img_list.append(i)
        num = min(len(label_list), len(img_list))
        for i in range(num):
            shutil.copy(os.path.join(dir, img_list[i]), os.path.join(img_dir, img_list[i]))
            shutil.copy(os.path.join(dir, label_list[i]), os.path.join(label_dir, label_list[i]))


def filesrename(path, dst_path, prefix='',postfix=None):
    """
    rename files orderly in the given directory.
    @param path: Given path
    """
    files = os.listdir(path)
    for i, file in enumerate(files):
        src = os.path.join(path, file)
        if postfix is None:
            postfix = file.split('.')[1]
        dst = os.path.join(dst_path, prefix + '{}.'.format(i) + postfix)
        os.rename(src, dst)


def cvtImgs(src, dst, postfix='jpg', dsize=None):
    """
    Given src & dst directory, iteratively convert the format of images
    into a given postfix format. If resize is specified as integer, then
    a resize ratio is specified, if given 2-array, then size is specified.
    @param src:
    @param dst:
    @param postfix:
    """
    files = os.listdir(src)
    for file in files:
        name = file.split('.')[0]
        img_path = os.path.join(src, file)
        img = cv2.imread(img_path)
        dst_path = os.path.join(dst, name + '.' + postfix)
        if isinstance(dsize, list) or isinstance(dsize, tuple):
            img = resize(img, dsize=dsize)
        elif dsize is not None:
            img = resize(img, ratio=dsize)
        cv2.imwrite(dst_path, img)

# img_path="D:/data/train_data/together/JPEGImages"
# txt_path="D:/data/train_data/together/ImageSets/Main"

# jpg_path="D:/data/train_data/together/JPEGImages"
# annot_path="D:/data/train_data/together/Annotations"
# remove_jpg_according_annot(annot_path,jpg_path)
# write_txt_random_sample(img_path,txt_path,1)
# mv_jpg_xml()

# path="D:\\zmhj_photo\\detection\\"
# separate_img_label(path,path+"img",path+"label")
