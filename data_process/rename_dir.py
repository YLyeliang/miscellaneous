import os

# Given root dir containing images and corresponding labels, rename all the file name from given number to given number.

root_dir="D:\\data\\AerialGoaf"
postfix="annot"
prefix="DJI_00"

dir_names=os.listdir(root_dir)
dir_images=[os.path.join(root_dir,dir) for dir in dir_names if not postfix in dir]

num=1
for i,img_dir in enumerate(dir_images):
    for file in os.listdir(img_dir):
        os.rename(os.path.join(img_dir,file),os.path.join(img_dir,prefix+"{}.png".format(num)))
        os.rename(os.path.join(img_dir+postfix,file),os.path.join(img_dir+postfix,prefix+"{}.png".format(num)))
        num+=1

