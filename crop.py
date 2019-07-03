import os
import numpy as np
from PIL import Image
from lxml import etree, objectify
import random
import shutil
root_path = "D:/data/stitch"
images_path = "D:/data/stitch/JPEGImages"
annots_path = "D:/data/stitch/Annotations"
# xml_path = "D:/data/stitch/Annotations/Line12_up_20190128023906_91_0km+968.1m_forward.xml"
out_xml = "D:/data/stitch/crop/Annotations"
out_crop = "D:/data/stitch/crop/JPEGImages"


# img_path = os.path.join(images_path, "Line12_up_20190128023906_91_0km+968.1m_forward.jpg")
# img =cv.imread(img_path)
# img = Image.open(img_path)
# img2 = img.crop((400, 0, 400+width, height))  # (left, upper, right, lower)

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
            E.name('water'),
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
        for annots in os.listdir(annots_path):
            count = 0
            # load annotation informations.
            img_name, bboxes, width, height = self.load_annot(os.path.join(annots_path, annots))
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

                # start crop.
                crop_xmin = np.random.randint(0, width - self.crop_width)
                crop_xmax = crop_xmin + self.crop_width

                # when crop,remove those very close patches.
                if len(x_arr) > 0:
                    dist = [abs(i - crop_xmin) for i in x_arr]
                    dist.sort()
                    if dist[0] < self.dist_cond:
                        continue

                # crop image
                img_crop = img.crop((crop_xmin, 0, crop_xmax, self.crop_height))
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

                    # 如果裁剪图片从box中间切开，且在box左边
                    if box_xmin < crop_xmin and box_xmax > crop_xmin:
                        cpbox_xmin = crop_xmin
                        cpbox_xmax = box_xmax
                    # 在box右边
                    elif box_xmin < crop_xmax and box_xmax > crop_xmax:
                        cpbox_xmin = box_xmin
                        cpbox_xmax = crop_xmax
                    # 包含box
                    else:
                        cpbox_xmin = box_xmin
                        cpbox_xmax = box_xmax
                    # set relative coordinate to crop image.
                    rel_xmin = cpbox_xmin - crop_xmin
                    rel_xmax = cpbox_xmax - crop_xmin
                    rel_ymin = box_ymin
                    rel_ymax = box_ymax
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


Crop_net = Random_crop(images_path, annots_path,
                       out_xml, out_crop, crop_time=500)
Crop_net.random_crop()


def random_sample(src_path,dst_path):
    # 从样本中随机抽取部分作为train和test,并移动到指定文件
    src_img_path = "D:\AerialGoaf/refine2/256x256/train"
    src_path = "D:\AerialGoaf/refine2/256x256/trainannot"
    dst_img_path = "D:\AerialGoaf/refine2/256x256/val"
    dst_path = "D:\AerialGoaf/refine2/256x256/valannot"
    # index=np.random.random_integers(3200,size=(200,))
    files = os.listdir("D:\AerialGoaf/refine2/256x256/trainannot")
    files = random.sample(files, 200)
    for i in files:
        src_img = os.path.join(src_img_path, i)
        src_mask = os.path.join(src_path, i)
        dst_img = os.path.join(dst_img_path, i)
        dst_mask = os.path.join(dst_path, i)
        shutil.move(src_img, dst_img)
        shutil.move(src_mask, dst_mask)

def write_txt(img_path,txt_path):
    img_files=os.listdir(img_path)
    