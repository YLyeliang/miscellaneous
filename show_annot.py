import os
import xml.etree.ElementTree as ET
import cv2

import numpy as np

# xml_path="./1_Line17_up_20190411032509_29_34km+484.4m_forward.xml"
annot_path="D:/data/stitch/crop/Annotations"
img_path = "D:/data/stitch/crop/JPEGImages"
out_path= "D:/data/visualization_leakageDataset/stitch"
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
    for bbox in bboxes:
        cv2.rectangle(img,(bbox[0],bbox[1]),(bbox[2],bbox[3]),color=(0,255,0),thickness=5)
        cv2.putText(img,"water",(bbox[0],bbox[3]),cv2.FONT_HERSHEY_COMPLEX,1,color=(0,0,255),thickness=2)
    if out is not None:
        cv2.imwrite(out,img)
    else:
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        cv2.imshow("image",img)
        cv2.waitKey()

for annot in os.listdir(annot_path):
    if annot is not '':
        img_name,bboxes = load_annot(os.path.join(annot_path,annot))
        img_name = img_name[:-3]+'jpg'
        show_img_annot(os.path.join(img_path,img_name),bboxes)

debug=1