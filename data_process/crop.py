import os
import numpy as np
from PIL import Image
from lxml import etree, objectify
import xml.etree.ElementTree as ET
import random
import shutil

# E = objectify.ElementMaker(annotate=False)
# anno_tree = E.annotation(
#     E.folder('VOC2007'),
#     E.filename("test.jpg"),
#     E.source(
#         E.database('Unknown')
#     ),
#     E.size(
#         E.width(800),
#         E.height(600),
#         E.depth(3)
#     ),
#     E.segmented(0),
# )
# subtree = E.object(
#     E.name('water'),
#     E.pose('Unspecified'),
#     E.truncated(0),
#     E.difficult(0),
#     E.bndbox(
#         E.xmin(1),
#         E.ymin(2),
#         E.xmax(3),
#         E.ymax(4)
#     )
# )
# anno_tree.append(subtree)
# etree.ElementTree(anno_tree).write("text.xml", pretty_print=True)

# tree.write("demo.xml",encoding='utf-8',xml_declaration=False)

def load_annot(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    size = root.find("size")
    width = int(size.find('width').text)
    height = int(size.find('height').text)
    img_name = root.find('filename').text
    bboxes = []
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
    return img_name, bboxes


class Random_crop(object):
    """
    Random crop images with annotated bboxes.
    Image path, annots path, out annots path, and out cropped image path should be given.
    The height and width of cropped image should be specified, and iteration time for a image
    should be specified, and the condtion
    """
    def __init__(self, images_path, annots_path, out_xmls, out_crops,
                 crop_width=2048, crop_height=4000, crop_time=50, dist_cond=500):
        self.images_path = images_path
        self.annots_path = annots_path
        self.out_xmls = out_xmls
        self.out_crops = out_crops
        self.crop_width = crop_width
        self.crop_height = crop_height
        self.crop_time = crop_time
        self.dist_cond = dist_cond

    def check_exist(self):
        if not os.path.exists(self.out_xmls):
            os.makedirs(self.out_xmls)
        if not os.path.exists(self.out_crops):
            os.makedirs(self.out_crops)

    def load_annot(self, xml_path):
        tree = ET.parse(xml_path)
        root = tree.getroot()
        size = root.find("size")
        width = int(size.find('width').text)
        height = int(size.find('height').text)
        img_name = root.find('filename').text
        bboxes = []
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
        return img_name, bboxes, width, height

    def init_xml(self, filename=None):
        if filename == None:
            raise ValueError("filename must be specified.")
        E = objectify.ElementMaker(annotate=False)
        anno_tree = E.annotation(
            E.folder('VOC2007'),
            E.filename(filename),
            E.source(
                E.database('Unknown')
            ),
            E.size(
                E.width(self.crop_width),
                E.height(self.crop_height),
                E.depth(3)
            ),
            E.segmented(0),
        )
        return anno_tree

    def write_box(self, tree, xmin, ymin, xmax, ymax):
        E = objectify.ElementMaker(annotate=False)
        subtree = E.object(
            E.name('crack'),
            E.pose('Unspecified'),
            E.truncated(0),
            E.difficult(0),
            E.bndbox(
                E.xmin(xmin),
                E.ymin(ymin),
                E.xmax(xmax),
                E.ymax(ymax)
            )
        )
        tree.append(subtree)
        return tree

    def random_crop(self):
        self.check_exist()
        for num,annots in enumerate(os.listdir(self.annots_path)):
            count = 0
            # load annotation informations.
            img_name, bboxes, width, height = self.load_annot(os.path.join(self.annots_path, annots))
            assert isinstance(width, int) and isinstance(height, int)

            # set image name and load image.
            img_name = img_name[:-3] + 'jpg'
            img_path = os.path.join(self.images_path, img_name)
            img = Image.open(img_path)
            # img_arr=np.array(img)

            x_arr = []
            for i in range(self.crop_time):
                # set xml and crop image name ,for save.
                crop_name = img_name[:-4] + '_{}'.format(count) + ".jpg"
                xml_name = img_name[:-4] + "_{}".format(count) + ".xml"
                xml_save = os.path.join(self.out_xmls, xml_name)
                crop_save = os.path.join(self.out_crops, crop_name)
                self.annot_tree = self.init_xml(crop_name)

                # start crop. Initialize cropped image patches.
                crop_xmin = np.random.randint(0, width - self.crop_width)
                crop_xmax = crop_xmin + self.crop_width
                crop_ymin = np.random.randint(0,height - self.crop_height)
                crop_ymax = crop_ymin+self.crop_height

                # when crop, remove those very close patches.
                if len(x_arr) > 0:
                    dist = [abs(i - crop_xmin) for i in x_arr]
                    dist.sort()
                    if dist[0] < self.dist_cond:
                        continue

                # crop image
                img_crop = img.crop((crop_xmin, crop_ymin, crop_xmax, crop_ymax))
                crop_bboxes = []
                # check boundary between box and crop image.
                for box in bboxes:
                    box_xmin = box[0]
                    box_xmax = box[2]
                    box_ymin = box[1]
                    box_ymax = box[3]
                    # if box not in crop image,continue.
                    if box_xmin >= crop_xmax or box_xmax <= crop_xmin:
                        continue
                    if box_ymin >= crop_ymax or box_ymax <=crop_ymin:
                        continue

                    # 如果裁剪图片从box中间切开，且在box右边
                    if box_xmin < crop_xmin and box_xmax > crop_xmin:
                        cpbox_xmin = crop_xmin
                        cpbox_xmax = box_xmax

                    # 在box左边
                    elif box_xmin < crop_xmax and box_xmax > crop_xmax:
                        cpbox_xmin = box_xmin
                        cpbox_xmax = crop_xmax
                    # 包含box
                    else:
                        cpbox_xmin = box_xmin
                        cpbox_xmax = box_xmax

                    # 判断y方向上的bbox与cropped image的交叠情况
                    # 如果裁剪图片从box中间切开，且在box下方
                    if box_ymin < crop_ymin and box_ymax > crop_ymin:
                        cpbox_ymin = crop_ymin
                        cpbox_ymax = box_ymax

                    # 在box上方
                    elif box_ymin < crop_ymax and box_ymax > crop_ymax:
                        cpbox_ymin = box_ymin
                        cpbox_ymax = crop_ymax
                    # 包含box
                    else:
                        cpbox_ymin = box_ymin
                        cpbox_ymax = box_ymax

                    # set relative coordinate to crop image.
                    rel_xmin = cpbox_xmin - crop_xmin
                    rel_xmax = cpbox_xmax - crop_xmin
                    rel_ymin = cpbox_ymin - crop_ymin
                    rel_ymax = cpbox_ymax - crop_ymin
                    crop_box = [rel_xmin, rel_ymin, rel_xmax, rel_ymax]
                    crop_bboxes.append(crop_box)

                # 只保存有框的图片
                if len(crop_bboxes) == 0:
                    continue

                x_arr.append(crop_xmin)
                for cpbox in crop_bboxes:
                    self.annot_tree = self.write_box(self.annot_tree, cpbox[0], cpbox[1], cpbox[2], cpbox[3])

                # write xml file.

                etree.ElementTree(self.annot_tree).write(xml_save, pretty_print=True)
                img_crop.save(crop_save)
                count += 1

            print("The {}th image cropped {} patches.".format(num,count))


