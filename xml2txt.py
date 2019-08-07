# coding=utf-8
#!/usr/bin/env python

import os
import re
import cv2
from xml.dom import *
import xml.dom.minidom
from xml.dom import minidom, Node
try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET
from skimage import io

headstr = """\
<annotation>
    <folder>VOC2007</folder>
    <filename>%s</filename>
    <source>
        <database>My Database</database>
        <annotation>PASCAL VOC2007</annotation>
        <image>flickr</image>
        <flickrid>NULL</flickrid>
    </source>
    <owner>
        <flickrid>NULL</flickrid>
        <name>company</name>
    </owner>
    <size>
        <width>%d</width>
        <height>%d</height>
        <depth>%d</depth>
    </size>
    <segmented>0</segmented>
"""
objstr = """\
    <object>
        <name>%s</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
            <xmin>%d</xmin>
            <ymin>%d</ymin>
            <xmax>%d</xmax>
            <ymax>%d</ymax>
        </bndbox>
    </object>
"""
tailstr = '''\
</annotation>
'''
def writexml(filename, head, bbxes, tail,width,height):
    f = open(filename, "w")
    f.write(head)
    for bbx in bbxes:
        if bbx[0]<0:
            bbx[0]=1
        if bbx[1]<0:
            bbx[1]=1
        if bbx[2]>width:
            bbx[2]=width-1
        if bbx[3]>height:
            bbx[3]=height-1
        # f.write(objstr % ('face', bbx[0], bbx[1], bbx[0] + bbx[2], bbx[1] + bbx[3]))
        f.write(objstr % ('water', bbx[0], bbx[1], bbx[2] , bbx[3]))
    f.write(tail)
    f.close()
def Xml_read(dom):
    root = dom.documentElement
    size = root.getElementsByTagName('size')
    width = size[0].getElementsByTagName('width')[0]
    width = int(width.childNodes[0].data)
    height = size[0].getElementsByTagName('height')[0]
    height = int(height.childNodes[0].data)
    depth = size[0].getElementsByTagName('depth')[0]
    #print 'width is {:3s},height is {:3s},depth is {:3s}'.format(width.childNodes[0].data,height.childNodes[0].data,depth.childNodes[0].data)
    objects = root.getElementsByTagName('object')
    xmin = [0]*len(objects)
    ymin = [0]*len(objects)
    xmax = [0]*len(objects)
    ymax = [0]*len(objects)
    object_num = len(objects)
    for i in range(0,object_num):
        object = objects[i].getElementsByTagName('bndbox')[0]
        xmin[i] = object.getElementsByTagName('xmin')[0]
        ymin[i] = object.getElementsByTagName('ymin')[0]
        xmax[i] = object.getElementsByTagName('xmax')[0]
        ymax[i] = object.getElementsByTagName('ymax')[0]

        xmin[i] = int(float(xmin[i].childNodes[0].data))
        ymin[i] = int(float(ymin[i].childNodes[0].data))
        xmax[i] = int(float(xmax[i].childNodes[0].data))
        ymax[i] = int(float(ymax[i].childNodes[0].data))
        #print 'xmin is {:3s},ymin is {:3s},xmax is {:3s},ymax is {:3s}'\
            #.format(xmin[i].childNodes[0].data,ymin[i].childNodes[0].data,xmax[i].childNodes[0].data,ymax[i].childNodes[0].data)
    return width,height,object_num,xmin,ymin,xmax,ymax

def Xml_write(fileName, width1, height1, objectNum, leftTopx, leftTopy, rightbottomx,rightbottomy):
    sampleType = 'water'
    doc = minidom.Document()

    # doc.appendChild(doc.createComment("Simple xml document__chapter 8"))

    # generate the annotation
    annotation = doc.createElement('annotation')
    doc.appendChild(annotation)

    # the title
    folder = doc.createElement('folder')
    folder.appendChild(doc.createTextNode("VOC2007"))
    annotation.appendChild(folder)

    filename = doc.createElement('filename')
    filename.appendChild(doc.createTextNode(fileName[0:-4] + '.jpg'))  # doc.createTextNode("000001.jpg")
    annotation.appendChild(filename)

    source = doc.createElement('source')
    annotation.appendChild(source)

    owner = doc.createElement('owner')
    annotation.appendChild(owner)

    size = doc.createElement('size')
    annotation.appendChild(size)

    segmented = doc.createElement('segmented')
    segmented.appendChild(doc.createTextNode("0"))
    annotation.appendChild(segmented)

    flickrid = doc.createElement('flickrid')
    flickrid.appendChild(doc.createTextNode("tv.sohu.com"))
    owner.appendChild(flickrid)

    name = doc.createElement('name')
    name.appendChild(doc.createTextNode("AI"))
    owner.appendChild(name)

    width = doc.createElement('width')
    width.appendChild(doc.createTextNode(str(width1)))
    size.appendChild(width)

    height = doc.createElement('height')
    height.appendChild(doc.createTextNode(str(height1)))
    size.appendChild(height)

    depth = doc.createElement('depth')
    depth.appendChild(doc.createTextNode("3"))
    size.appendChild(depth)
    for i in range(0, objectNum):
        object = doc.createElement('object')
        annotation.appendChild(object)

        name = doc.createElement('name')
        name.appendChild(doc.createTextNode(str(sampleType)))
        object.appendChild(name)

        pose = doc.createElement('pose')
        pose.appendChild(doc.createTextNode(str(0)))  # "Unspecified"
        object.appendChild(pose)

        truncated = doc.createElement('truncated')
        truncated.appendChild(doc.createTextNode("0"))
        object.appendChild(truncated)

        difficult = doc.createElement('difficult')
        difficult.appendChild(doc.createTextNode("0"))
        object.appendChild(difficult)

        bndbox = doc.createElement('bndbox')
        object.appendChild(bndbox)

        xmin = doc.createElement('xmin')
        xmin.appendChild(doc.createTextNode(str(leftTopx[i])))
        bndbox.appendChild(xmin)

        ymin = doc.createElement('ymin')
        ymin.appendChild(doc.createTextNode(str(leftTopy[i])))
        bndbox.appendChild(ymin)

        xmax = doc.createElement('xmax')
        xmax.appendChild(doc.createTextNode(str(rightbottomx[i])))
        bndbox.appendChild(xmax)

        ymax = doc.createElement('ymax')
        ymax.appendChild(doc.createTextNode(str(rightbottomy[i])))
        bndbox.appendChild(ymax)
    database = doc.createElement('database')
    database.appendChild(doc.createTextNode("The VOC2007 Database"))
    source.appendChild(database)

    annotation = doc.createElement('annotation')
    annotation.appendChild(doc.createTextNode("PASCAL VOC2007"))
    source.appendChild(annotation)

    image = doc.createElement('image')
    image.appendChild(doc.createTextNode("flickr"))
    source.appendChild(image)

    flickrid = doc.createElement('flickrid')
    flickrid.appendChild(doc.createTextNode("NULL"))
    source.appendChild(flickrid)
    # print doc.toprettyxml()
    f = file('D:/work/baijia_work/data/water/20190206/Annotations_new/'+fileName, 'w')
    doc.writexml(f, '', ' ', '\n', 'utf-8')
    f.close()
xml_dir = 'D:/work/baijia_work/data/face/widerface/Annotations/'
img_dir = '/data3/AIData/widerface/JPEGImages/'
res_dir = 'D:/work/baijia_work/data/face/widerface/'
respath = res_dir+'widerface_min15gth.txt'
resfile = open(respath,'w')
list = os.listdir(xml_dir)
for ii in range(0,len(list)):
    imgname = list[ii]
    xml_path = xml_dir+imgname
    # img = cv2.imread(img_path)
    imgnamenew = imgname.replace('.xml','.jpg')
    respath = img_dir+imgnamenew
    dom = xml.dom.minidom.parse(xml_path)
    width, height, object_num, xmin, ymin, xmax, ymax = Xml_read(dom)
    out = respath+' '+str(object_num)
    flag = 0
    for i in range(0, object_num):
        if xmin[i]<=0:
            xmin[i] = 1
        if ymin[i]<=0:
            ymin[i] = 1
        if xmax[i]>=width:
            xmax[i] = width-1
        if ymax[i]>=height:
            ymax[i]= height-1
        xmin[i] = int(float(xmin[i]))
        ymin[i] = int(float(ymin[i]))
        xmax[i] = int(float(xmax[i]))
        ymax[i] = int(float(ymax[i]))
        w  = xmax[i]-xmin[i]
        h = ymax[i]-ymin[i]
        out = out + ' '+ str(xmin[i])+ ' '+ str(ymin[i])+ ' '+ str(w)+ ' '+ str(h)
        if w < 15 or h < 15:
            flag = 1
            break
    if flag == 0:
        out = out + '\n'
        resfile.write(out)
resfile.close()


# face_num = 0
# minw=10000
# minh = 10000
# maxw = 0
# maxh = 0
# minwlst=[1000,1000]
# minhlst=[1000,1000]
# maxwlst=[1000,1000]
# maxhlst=[1000,1000]
# minarea=[10000000,0]
# for ii in range(0,len(list)):
#     imgname = list[ii]
#     img_path = img_dir+imgname
#     img = cv2.imread(img_path)
#     h, w, _ = img.shape
#     xmlname = imgname.replace('.jpg','.xml')
#     path = os.path.join(xml_dir,xmlname)
#     filename = os.path.basename(path)
#     print(filename)
#     dom = xml.dom.minidom.parse(path)
#
#     #ff = open('./toujian_result.txt', 'a')
#     width,height,object_num,xmin,ymin,xmax,ymax=Xml_read(dom)
#     width = w
#     height = h
#     im = io.imread(img_path)
#     head = headstr % (xmlname, im.shape[1], im.shape[0], im.shape[2])
#     #print width,height,object_num,xmin,ymin,xmax,ymax
#     # object_newnum = 0
#     # left_wxt = [0]*1000
#     # top_wxt = [0]*1000
#     # right_wxt = [0]*1000
#     # bottom_wxt = [0]*1000
#     #ff.write(str(filename) + ' '+str(object_num) + ' ')
#     print(path)
#     print(width,height)
#     bbxes = []
#     for i in range(0,object_num):
#         bbx = []
#         if xmin[i]<=0:
#             print("boxes left :")
#             print(xmin[i])
#         if ymin[i]<=0:
#             print("boxes top :")
#             print(ymin[i])
#         if xmax[i]>=width:
#             print("boxes right :")
#             print(xmax[i])
#         if ymax[i]>=height:
#             print("boxes bottom :")
#             print(ymax[i])
#         xmin[i] = int(float(xmin[i]))
#         ymin[i] = int(float(ymin[i]))
#         xmax[i] = int(float(xmax[i]))
#         ymax[i] = int(float(ymax[i]))
#         bbx.append(xmin[i])
#         bbx.append(ymin[i])
#         bbx.append(xmax[i])
#         bbx.append(ymax[i])
#         # for i in range(6):
#         #     bbx.append(0)
#         bbxes.append(bbx)
#
#         # thick = int((h + w) / 300)
#         # cv2.rectangle(img,(xmin[i], ymin[i]), (xmax[i], ymax[i]),[0, 0, 255], thick)
#     xmlnewpath = os.path.join(res_dir,xmlname)
#     writexml(xmlnewpath, head, bbxes, tailstr,width,height)
    # img = cv2.resize(img,(512, 512), interpolation=cv2.INTER_CUBIC)
    # cv2.imwrite(os.path.join(res_dir,imgname.replace('.bmp','.jpg')),img)




    #     if w <= 20 or h <= 20:
    #         print filename,xmin[i],ymin[i],xmax[i],ymax[i],w,h
    #         object_newnum = 0
    #         #continue
    #         break
    #     if xmin[i] <= 0:
    #         xmin[i] = 0
    # if ymin[i] <= 0:
    #         ymin[i] = 0
    #
    #     if xmax[i] >= width:
    #         xmax[i] = int(width -1)
    #     if ymax[i] >= height:
    #         ymax[i] = int(height -1)
    #     left_wxt[object_newnum] = xmin[i]
    #     top_wxt[object_newnum] = ymin[i]
    #     right_wxt[object_newnum] = xmax[i]
    #     bottom_wxt[object_newnum] = ymax[i]
    #     object_newnum = object_newnum + 1
    #     #ff.write(str(xmin[i])+ ' '+str(ymin[i])+' '+str(xmax[i]-xmin[i])+' '+str(ymax[i]-ymin[i])+' '+str(0)+' ')
    # #ff.write('\n')
    # #ff.close()
    # face_num = face_num + object_newnum
    # print 'face_num',face_num
    # if object_newnum != 0:
    #     Xml_write(filename, width, height, object_newnum, left_wxt, top_wxt, right_wxt,bottom_wxt)

