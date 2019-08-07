import os
import shutil
from lxml import etree, objectify


class FormTransForm(object):
    def __init__(self,type='txt2xml'):
        self.type=type


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
                E.width(2048),
                E.height(4000),
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

    def txt2xml(self,txt,xml_outpath='./'):
        if not os.path.exists(xml_outpath):
            os.mkdir(xml_outpath)
        f=open(txt,'r')
        while True:
            line=f.readline()[:-1]
            if not line:
                break
            # write your transform code here.
            line_list=line.split(' ')
            xml_name=line_list[0].split('/')[1][:-3]+'xml'
            if len(line_list) >1:   # means have bbox
                tree=self.init_xml(line_list[0])
                for box_id in range(0,int((len(line_list)-2)/5)):
                    bbox = [int(i)  for i in line_list[2+box_id*5:6+box_id*5]]
                    tree = self.write_box(tree,bbox[0],bbox[1],bbox[2],bbox[3])
            else:
                tree=self.init_xml(line_list[0])
            etree.ElementTree(tree).write(os.path.join(xml_outpath,xml_name),pretty_print=True)



transform=FormTransForm()
for i in range(1,8):
    transform.txt2xml(txt='D:/data/Camera/Camera{}_yes.txt'.format(i),xml_outpath='D:/data/Camera/Camera{}_annot'.format(i))





