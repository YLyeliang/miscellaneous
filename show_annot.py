import os
import xml.etree.ElementTree as ET
import cv2

import numpy as np

# xml_path="./1_Line17_up_20190411032509_29_34km+484.4m_forward.xml"
annot_path="D:\zmhj_photo\detection\label"
img_path = "D:\zmhj_photo\detection\img"
out_path= "D:\zmhj_photo\detection\gt"
def load_annot(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    size = root.find("size")
    width = int(size.find('width').text)
    height = int(size.find('height').text)
    img_name= root.find('filename').text
    bboxes =[]
    for obj in root.findall("object"):
        name = obj.find('name').text
        difficult = int(obj.find('difficult').text)
        bnd_box = obj.find('bndbox')
        bbox = [
            int(bnd_box.find('xmin').text),
            int(bnd_box.find('ymin').text),
            int(bnd_box.find('xmax').text),
            int(bnd_box.find('ymax').text)
        ]
        bboxes.append(bbox)
    return img_name,bboxes

def show_img_annot(img_path,bboxes,out=None):
    img = cv2.imread(img_path)
    if img is None: return None
    for bbox in bboxes:
        cv2.rectangle(img,(bbox[0],bbox[1]),(bbox[2],bbox[3]),color=(0,0,255),thickness=2)
        cv2.putText(img,"crack",(bbox[0],bbox[1]),cv2.FONT_HERSHEY_COMPLEX,1,color=(255,255,255),thickness=1)
    if out is not None:
        cv2.imwrite(out,img)
    else:
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        cv2.imshow("image",img)
        cv2.waitKey()

# 加载文件夹内的所有Annot文件，并进行标注
# for annot in os.listdir(annot_path):
#     if annot is not '':
#         img_name,bboxes = load_annot(os.path.join(annot_path,annot))
#         img_name = img_name[:-3]+'jpg'
#         show_img_annot(os.path.join(img_path,img_name),bboxes,out=os.path.join(out_path,img_name))

# 加载文件夹内的所有预测文件，并将GT标注在上面
for img in os.listdir(img_path):
    img_name,bboxes = load_annot(os.path.join(annot_path,img[:-3]+'xml'))
    show_img_annot(os.path.join(img_path,img),bboxes,out=os.path.join(out_path,img))

debug=1