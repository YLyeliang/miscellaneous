import os
from PIL import Image
import numpy as np
import shutil
import random
import cv2

def random_remove():
    img_path="D:\data\\detail\\bg"
    annot_path="D:\data\\detail\\bgannot"
    files = os.listdir(img_path)

    files = random.sample(files, 71)
    for file in files:
        img=os.path.join(img_path,file)
        label=os.path.join(annot_path,file)
        os.remove(img)
        os.remove(label)

# random_remove()

def random_move(src_img,src_lab,dst_img,dst_lab):
    files = os.listdir(src_img)
    files = random.sample(files, 225)
    if not os.path.exists(dst_img):
        os.makedirs(dst_img)
    if not os.path.exists(dst_lab):
        os.makedirs(dst_lab)
    for file in files:
        img=os.path.join(src_img,file)
        label=os.path.join(src_lab,file)
        img_out=os.path.join(dst_img,file)
        lab_out=os.path.join(dst_lab,file)
        shutil.move(img,img_out)
        shutil.move(label,lab_out)

# random_move("D:\AerialGoaf\detail\\512x512\siteB","D:\AerialGoaf\detail\\512x512\siteBlab",
#             "D:\AerialGoaf\detail\\512x512\siteBval","D:\AerialGoaf\detail\\512x512\siteBvalannot")

def preserve_patch_higher_prob(img_path,lab_path,img_out,lab_out,ratio):
    """
    copy images that the crack ratio higher than the overall ratio.
    """
    if not os.path.exists(img_out):
        os.makedirs(img_out)
    if not os.path.exists(lab_out):
        os.makedirs(lab_out)
    for file in os.listdir(lab_path):
        mask=Image.open(os.path.join(lab_path,file))
        # mask=Image.open("D:\AerialGoaf\detail\\512x512\label\\00_9.png")
        mask=np.array(mask).flatten()
        cracks=np.sum(mask)             # 裂缝像素数
        backgrounds=mask.shape[0]       # 背景像素数
        rate=cracks/backgrounds         # 裂缝占比
        if rate>= ratio:
            shutil.copy(os.path.join(img_path,file),os.path.join(img_out,file))
            shutil.copy(os.path.join(lab_path,file),os.path.join(lab_out,file))

# img_path="D:\AerialGoaf\detail\\resource\\siteB512\\image"
# lab_path="D:\AerialGoaf\detail\\resource\\siteB512\\label"
# img_out ="D:\AerialGoaf\detail\\resource\\siteB512\\siteBimg"
# lab_out ="D:\AerialGoaf\detail\\resource\\siteB512\\siteBlab"
# preserve_patch_higher_prob(img_path,lab_path,img_out,lab_out,0.005)

crop_size=512
slide_pixel=128
# 对图片进行随机裁剪，裁剪出512X512的图片
# for i in os.listdir(testpath):
#     image=Image.open(os.path.join(testpath,i))
#     width,height=image.size
#     mask=Image.open(os.path.join(testannotpath,i))
#     for j in range(40):
#         xa1=random.randint(0,width-crop_size)
#         ya1=random.randint(0,height-crop_size)
#         xa2=xa1+crop_size
#         ya2=ya1+crop_size
#         rect_image=image.crop([xa1,ya1,xa2,ya2])
#         rect_mask=mask.crop([xa1,ya1,xa2,ya2])
#         if not os.path.exists(outpath):
#             os.mkdir(outpath)
#         rect_image.save(os.path.join(outpath,i.split('.')[0]+'_{}.'.format(j)+'png'))
#         if not os.path.exists(outannotpath):
#             os.mkdir(outannotpath)
#         rect_mask.save(os.path.join(outannotpath,i.split('.')[0]+'_{}.'.format(j)+'png'))


def sliding_crop():
    outpath="D:\AerialGoaf\detail\\resource\\siteB512\\image"
    outannotpath="D:\AerialGoaf\detail\\resource\\siteB512\\label"
    imagepath="D:\AerialGoaf\detail\\resource\\site2"
    labelpath="D:\AerialGoaf\detail\\resource\\site2label"
    # 滑动窗口裁剪
    for i in os.listdir(imagepath):
        image=Image.open(os.path.join(imagepath,i))
        width,height=image.size
        mask=Image.open(os.path.join(labelpath,i))
        xa1=0
        ya1=0
        slide_No=0
        end_of_x = 0  # 判断滑动窗口在x轴是否滑动完
        end_of_y = 0
        while(True):
            xa2=xa1+crop_size
            ya2=ya1+crop_size
            rect_image=image.crop([xa1,ya1,xa2,ya2])
            rect_mask=mask.crop([xa1,ya1,xa2,ya2])
            if not os.path.exists(outpath):
                os.makedirs(outpath)
            rect_image.save(os.path.join(outpath, i.split('.')[0] + '_{}.'.format(slide_No) + 'png'))
            if not os.path.exists(outannotpath):
                os.makedirs(outannotpath)
            rect_mask.save(os.path.join(outannotpath, i.split('.')[0] + '_{}.'.format(slide_No) + 'png'))
            xa1+=slide_pixel
            slide_No+=1
            if (xa1>(width-crop_size))&(end_of_x==0):      #当滑动窗口第一次超过图像区域，则将滑动窗口重置到最右侧
                xa1=width-crop_size
                end_of_x+=1
            elif (xa1>(width-crop_size))&(end_of_x==1):    #若第二次时则在y方向上+100像素，重置到最左侧
                xa1=0
                ya1+=slide_pixel
                end_of_x =0
                if (ya1>(height-crop_size))&(end_of_y==0):
                    ya1=height-crop_size
                    end_of_y+=1
                elif(ya1>(height-crop_size))&(end_of_y==1):
                    end_of_y=0
                    break
# sliding_crop()

# construct site A & B dataset A for training, B for test and vice versa
def mv_file_with_prefix(src_path,src_lab_path,dst_path, dst_lab_path,prefix_path):
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)
    if not os.path.exists(dst_lab_path):
        os.makedirs(dst_lab_path)
    prefix=os.listdir(prefix_path)
    prefix=[i.split('.')[0] for i in prefix]
    files=os.listdir(src_path)
    for file in files:
        if file.split('_')[0] in prefix:
            src_file=os.path.join(src_path,file)
            lab_file=os.path.join(src_lab_path,file)
            dst_file=os.path.join(dst_path,file)
            dst_lab_file=os.path.join(dst_lab_path,file)
            shutil.copy(src_file,dst_file)
            shutil.copy(lab_file,dst_lab_file)

# mv_file_with_prefix("D:\AerialGoaf\detail\\512x512\image","D:\AerialGoaf\detail\\512x512\label",
#                     "D:\AerialGoaf\detail\\512x512\\siteB","D:\AerialGoaf\detail\\512x512\\siteBlab","D:\AerialGoaf\detail\\resource\site2")

# because uint16 is not fit for msi_fcn, so it should convert to uint8.
def convert_uint16_to_uint8(path):
    files=os.listdir(path)
    for file in files:
        img=Image.open(os.path.join(path,file))
        array=np.array(img)
        array= array.astype(np.uint8)
        image=Image.fromarray(array)
        image.save(os.path.join(path,file))
        # cv2.imwrite(os.path.join(path,file),img)
convert_uint16_to_uint8("D:\AerialGoaf\detail\\512x512\siteBvalannot")