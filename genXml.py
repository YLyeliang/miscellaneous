# coding:utf-8
import os
import shutil
import cv2
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
        \] 
        <manned>%d</manned>
        <bndbox>
            <xmin>%d</xmin>
            <ymin>%d</ymin>
            <xmax>%d</xmax>
            <ymax>%d</ymax>
        </bndbox>
    </object>
"""
headstr_dong = """\
<annotation>
    <folder>%s</folder>
    <filename>%s</filename>
    <path>%s</path>
    <source>
        <database>Unkonwn</database>
    </source>
    <size>
        <width>%d</width>
        <height>%d</height>
        <depth>%d</depth>
    </size>
    <segmented>0</segmented>
"""
objstr_dong = """\
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


def filter_car_face():
    rootdir = 'D:/work/carPro/20181129_carface_3w/baoji8/'
    imgdir = rootdir+'pic/'
    filepath = rootdir+'face_results.txt'
    resdir = rootdir+'filter/2&&0.6_0.7_2all/'

    file = open(filepath,'r')
    lines = file.readlines()
    file.close()
    for line in lines:
        info = line.strip().split()
        imgname = info[0]
        facenum = int(info[1])
        # if facenum == 0:
        #     oripath = imgdir+imgname
        #     dstpath = resdir+imgname
        #     shutil.copy(oripath,dstpath)
        # if facenum ==2 and float(info[6]) >= 0.6 and float(info[6]) < 0.7:
        if facenum == 2 and (float(info[6]) >= 0.6 and float(info[6]) < 0.7) and (float(info[11]) >= 0.6 and float(info[11]) < 0.7):
            oripath = imgdir + imgname
            dstpath = resdir + imgname
            shutil.copy(oripath, dstpath)
def checkFaceXML():
    rootdir = 'D:/work/carPro/face/data/jingsaishuju/tricycle/manned1/'
    resdir = 'D:/work/carPro/face/data/jingsaishuju/tricycle/res_manned1/'
    files = os.listdir(rootdir)
    xml_res_path = 'D:/work/carPro/face/data/jingsaishuju/tricycle/manned_1_newxml/manned_1_newxml/tricycle_box_anno_m1.txt'
    xmlfile = open(xml_res_path,'r')
    lines = xmlfile.readlines()
    xmlfile.close()

    infodic = dict()
    for line in lines:
        info = line.strip().split()
        name = info[0]
        if not infodic.has_key(name):
            infodic[name]=info
        else:
            print("name same "+name)
    cnt = 0
    totalcnt = len(files)
    for file in files:
        if infodic.has_key(file):
            if cnt%200 == 0:
                print(totalcnt-cnt)
            cnt+=1
            imgpath = os.path.join(rootdir,file)
            if os.path.exists(imgpath):
                respath = os.path.join(resdir, file)
                if os.path.exists(respath):
                    continue
                img = cv2.imread(imgpath)
                info = infodic[file]
                facenum = int(info[1])
                for i in range(facenum):
                    left = int(info[2+i*4])
                    top = int(info[2 + i * 4+1])
                    right = int(info[2 + i * 4+2])
                    bottom = int(info[2 + i * 4+3])
                    cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
                respath = os.path.join(resdir,file)
                cv2.imwrite(respath,img)

def cropFace():
    rootdir = 'D:/work/carPro/20181129_carface_3w/baoji8/pic/'
    resdir = 'D:/work/carPro/20181129_carface_3w/baoji8/cropFaces/'
    files = os.listdir(rootdir)
    xml_res_path = 'D:/work/carPro/20181129_carface_3w/baoji8/face_box_anno_xml.txt'
    xmlfile = open(xml_res_path, 'r')
    lines = xmlfile.readlines()
    xmlfile.close()

    infodic = dict()
    for line in lines:
        info = line.strip().split()
        name = info[0]
        if not infodic.has_key(name):
            infodic[name] = info
        else:
            print("name same " + name)
    cnt = 0
    totalcnt = len(files)
    for file in files:
        if infodic.has_key(file):
            if cnt % 200 == 0:
                print(totalcnt - cnt)
            cnt += 1
            imgpath = os.path.join(rootdir, file)
            if os.path.exists(imgpath):
                # (name,expend)=os.path.split(file)

                respath = os.path.join(resdir, file)
                if os.path.exists(respath):
                    continue
                img = cv2.imread(imgpath)
                height, width, _ = img.shape

                info = infodic[file]
                facenum = int(info[1])

                for i in range(facenum):
                    left = int(info[2 + i * 4])
                    top = int(info[2 + i * 4 + 1])
                    right = int(info[2 + i * 4 + 2])
                    bottom = int(info[2 + i * 4 + 3])
                    imgcx = int(width/2)
                    box_cx = (left+right)/2
                    box_cy = (top+bottom)/2
                    imgcy = int(height/2)

                    left_new = imgcx
                    top_new = 0
                    right_new = width-1
                    bottom_new = imgcy


                    if bottom > imgcy:
                        step = bottom-imgcy
                        step_top = top
                        if step_top < top:
                            step_h = int((top - step_top)*1.5)
                            top_new += step_h
                            bottom_new += step_h
                    if box_cx > imgcx:
                        left_new = imgcx
                        if left_new < left:
                            left_new = left - 5
                        right_new = width - (left_new-left)
                        top_new = max(0,top_new)
                        bottom_new = min(bottom_new,height-1)
                    else:
                        left_new = 0
                        right_new = imgcx
                        if right> right_new:
                            right_new = right
                        left_new = right-right_new
                        top_new = max(0, top_new)
                        bottom_new = min(bottom_new, height - 1)
                    imgcrop = img[top_new:bottom_new,left_new:right_new]
                    boxleft_new = left - left_new
                    boxtop_new = top - top_new
                    right_new  = boxleft_new+(right - left+1)
                    bottom_new = boxtop_new+(bottom-top+1)
                    cv2.rectangle(imgcrop, (boxleft_new, boxtop_new), (right_new, bottom_new), (0, 255, 0), 2)
                    # cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
                respath = os.path.join(resdir, file)
                cv2.imwrite(respath, imgcrop)

def filterFace():
    rootdir = 'D:/work/carPro/20181129_carface_3w/baoji8/'
    imgdir = rootdir + 'pic/'
    filepath = rootdir + 'face_results.txt'
    resdir = rootdir + 'filter_res/'

    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()
    picfiledic = dict()

    dirs = os.listdir(rootdir+'filter')
    for dir in dirs:
        subdir = os.path.join(rootdir,'filter',dir)
        imgfiles = os.listdir(subdir)
        for imfile in imgfiles:
            if not picfiledic.has_key(imfile):
                picfiledic[imfile]=imfile
    fnum = 0
    rnum = 0
    for line in lines:
        info = line.strip().split()
        imgname = info[0]
        facenum = int(info[1])
        img = cv2.imread(os.path.join(imgdir,imgname))
        if picfiledic.has_key(imgname):
            fnum+=1
            continue
        rnum+=1
        for i in range(facenum):
            left = float(info[2+i*5])
            top = float(info[2+i*5+1])
            right  = float(info[2+i*5+2])
            bottom = float(info[2 + i * 5 + 3])
            score = float(info[2 + i * 5 + 4])
            if score > 0.7:
                cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (0, 255, 0), 2)
        cv2.imwrite(resdir+imgname,img)
    print('filter num = '+str(fnum)+', rest num = '+str(rnum))
def renamefile():
    rootdir = 'D:/work/carPro/face/data/'
    oridir = rootdir+'face20181213/'
    resdir = rootdir + 'carface01/'
    f=  open(rootdir+'namelst.txt','w')
    files = os.listdir(oridir)
    for file in files:
        (filename, extension) = os.path.splitext(file)
        xmlpath = os.path.join(oridir,filename+'.xml')
        imgpath = os.path.join(oridir,filename+'.jpg')
        if os.path.exists(xmlpath) and os.path.exists(imgpath):
            newname = '1c'+filename
            resxmlpath = os.path.join(rootdir,newname+'.xml')
            resimgpath = os.path.join(rootdir, newname+'.jpg')
            f.write(newname+'\n')
            if os.path.exists(resxmlpath) and os.path.exists(resimgpath):
                continue
            shutil.copy(xmlpath, resxmlpath)
            shutil.copy(imgpath,resimgpath)
    f.close()
import random

def randomlist():
    rootdir = 'D:/work/carPro/face/Wider_Face/'
    orilst = rootdir+'train_car1_car2.txt'
    reslst = rootdir+'train_car1_car2_random.txt'
    resf = open(reslst,'w')
    orifile = open(orilst,'r')
    orilines = orifile.readlines()
    orifile.close()
    random.shuffle(orilines)
    resf.writelines(orilines)
    resf.close()

def mergeLable_Anno():
    imgdir = 'D:/work/carPro/face/data/filter_check_xml-1213/'
    files = os.listdir(imgdir)
    annopath = 'D:/work/carPro/20181129_carface_3w/baoji8/face_box_anno_xml.txt'
    anf = open(annopath,'r')
    lines = anf.readlines()
    anf.close()
    mergeresult =imgdir+ 'merge_anno_bbox.txt'
    resf = open(mergeresult,'w')
    andic =dict()
    for line in lines:
        info = line.strip().split()
        imgname = info[0]
        boxinfo = info[2:]
        ibox = [int(i) for i in boxinfo]

        if not andic.has_key(imgname):
            andic[imgname]= ibox
    for file in files:
        if file.find('.jpg')!=-1:
            imgpath = imgdir+file
            xmlpath = imgpath.replace('.jpg','.xml')
            if os.path.exists(xmlpath):
                w, h, fl = read_xml_ztc(xmlpath)
                if andic.has_key(file):
                    ibox = andic[file]
                    fl.append(ibox)
                out = file+' '+str(len(fl))
                for i in range(len(fl)):
                    for j in range(4):
                        out = out+' '+str(fl[i][j])
                out += '\n'
            else:
                if andic.has_key(file):
                    ibox = andic[file]
                    out = file + ' 1'
                    for j in range(4):
                        out = out + ' ' + str(ibox[j])
                out += '\n'
            resf.write(out)
    resf.close()

def checkRect():
    imgdir = 'D:/work/carPro/20181129_carface_3w/baoji8/pic/'
    lstpath = 'D:/work/carPro/face/data/filter_check_xml-1213/merge_anno_bbox.txt'
    file = open(lstpath,'r')
    lines = file.readlines()
    file.close()

    for line in lines:
        info = line.strip().split()
        imgname = info[0]
        imgpath = imgdir+imgname
        img = cv2.imread(imgpath)
        facenum = int(info[1])
        for i in range(facenum):
            left = int(info[2+i*4])
            top = int(info[2 + i * 4+1])
            right = int(info[2 + i * 4+2])
            bottom = int(info[2 + i * 4+3])
            cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.imshow("img",img)
        cv2.waitKey()
def writexml(idx, head, bbxes, tail,respath):
    filename = respath+"/2c%06d.xml" % (idx)
    f = open(filename, "w")
    f.write(head)
    for bbx in bbxes:
        if bbx[0]<1:
            bbx[0]=1
        if bbx[1]<1:
            bbx[1]=1
        if bbx[2]<10:
            continue
        if bbx[3]<10:
            continue
        # f.write(objstr % ('face', bbx[0], bbx[1], bbx[0] + bbx[2], bbx[1] + bbx[3]))
        f.write(objstr % ('face', bbx[0], bbx[1], bbx[2] , bbx[3]))
    f.write(tail)
    f.close()
def txt2xml_face():
    imgdir = 'D:/work/carPro/20181129_carface_3w/baoji8/pic/'
    lstpath = 'D:/work/carPro/face/data/filter_check_xml-1213/merge_anno_bbox.txt'
    resdir = 'D:/work/carPro/face/data/carface02/'
    file = open(lstpath, 'r')
    lines = file.readlines()
    file.close()
    idx = 0
    for line in lines:
        print(line)
        idx+=1
        info = line.strip().split()
        imgname = info[0]
        imgpath = imgdir + imgname
        img = cv2.imread(imgpath)
        facenum = int(info[1])
        im = io.imread(imgpath)
        head = headstr % (idx, im.shape[1], im.shape[0], im.shape[2])
        nums = int(info[1])
        bbxes = []
        for i in range(int(nums)):
            bbx=[]
            left = int(info[2 + i * 4])
            top = int(info[2 + i * 4 + 1])
            right = int(info[2 + i * 4 + 2])
            bottom = int(info[2 + i * 4 + 3])
            bbx.append(left)
            bbx.append(top)
            bbx.append(right)
            bbx.append(bottom)
            for i in range(6):
                bbx.append(0)
            bbxes.append(bbx)

        writexml(idx, head, bbxes, tailstr,resdir)
        resimgpath = resdir + "/2c%06d.jpg" % (idx)
        cv2.imwrite(resimgpath,img)
def genlist():

    xmldir = 'D:/work/carPro/face/data/1214/Annotations/'
    files = os.listdir(xmldir)

    namlst = open(xmldir+'train_slc.txt','w')
    for file in files:
        if file.find('.xml')!=-1:
            name = file.replace('.xml','')
            xmlname=name+'.xml'
            # if not os.path.exists(xmldir+xmlname):
            namlst.write(name+'\n')
    namlst.close()



def xml2gth():
    xmldir = 'D:/work/carPro/face/data/carface02/'
    subdir  ='carface02/'
    resf = open(xmldir+'carface02_train_bbox_gth.txt','w')
    files = os.listdir(xmldir)
    for file in files:
        if file.find('.xml')!=-1:
            xmlpath = xmldir+file
            imgpath = xmlpath.replace('.xml','.jpg')
            try:
                img = cv2.imread(imgpath)
            except:
                print(imgpath+' , imread erro')
                continue
            w, h, fl = read_xml(xmlpath)
            subpath = subdir+file.replace('.xml','.jpg')
            num  = len(fl)
            resf.write(subpath+'\n')
            resf.write(str(num)+'\n')
            for i in range(num):
                out = str(fl[i][0])+' '+str(fl[i][1])+' '+str(fl[i][2]-fl[i][0])+' '+str(fl[i][3]-fl[i][1])+' 0 0 0 0 0 0\n'
                resf.write(out)
    resf.close()

def filterxml():

    rootdir = 'D:/work/carPro/face/data/jingsaishuju/slagcar/filter_list/'
    imgdir = rootdir+'merge/'
    xmldir = 'D:/work/carPro/face/data/jingsaishuju/tricycle/xml_all/'
    train_lst = rootdir+'train_lst_slc_1.txt'
    f = open(train_lst,'w')
    imgfiles = os.listdir(imgdir)
    # xmlfiles = os.listdir(xmldir)
    for file in imgfiles:
        name = file.replace('.jpg','')
        f.write(name+'\n')
        xmlname = name+'.xml'
        xmlpath = xmldir+xmlname
        if os.path.exists(xmlpath):
            shutil.copy(xmlpath,imgdir+xmlname)
        else:
            print(xmlpath+' is not exists')

    f.close()
def filter_ztc_xml():
    xmldir = 'D:/work/carPro/face/data/jingsaishuju/slagcar/xml/'
    rootdir = 'D:/work/carPro/face/data/jingsaishuju/slagcar/filter_list/'
    filepath = rootdir+'merge_lable_right.txt'
    file= open(filepath,'r')
    lines = file.readlines()
    file.close()
    resdir = rootdir+'Annotations/'
    trainlst = rootdir+'train_ztc.txt'
    trainfile = open(trainlst,'w')
    for line in lines:
        info = line.strip()
        name = info.replace('.jpg','')
        orixmlpath = xmldir+name+'.xml'
        if os.path.exists(orixmlpath):
            # shutil.copy(orixmlpath,resdir+name+'.xml')
            trainfile.write(name+'\n')
    trainfile.close()
def read_xml_label(xml_path):
    tree = ET.parse(xml_path)  # 加载xml文档
    root = tree.getroot()  # 获取根元素
    # tag_root = root.tag  # 元素名字（格式：字符串）
    # attr_root = root.attrib  # 元素属性（格式：字典，{属性名1:属性值1, 属性名2:属性值2, 属性名3:属性值3...}）
    size = root.findall("size")[0]
    w = int(size.find("width").text)
    h = int(size.find("height").text)
    d = int(size.find("depth").text)
    face_list = []
    for face in root.findall("object"):
        box = face.find("bndbox")
        manned_name  = face.find('name').text
        if manned_name == 'car_Person' or manned_name == 'car_person':
            manned = 1
        elif manned_name == 'car_noPerson' or manned_name == 'car_noperson':
            manned = 0
        sbox = [box.find('xmin').text, box.find('ymin').text, box.find('xmax').text, box.find('ymax').text]
        # ibox = [box.find('xmin'), box.find('ymin'), box.find('xmax'), box.find('ymax')]
        ibox = [int(i) for i in sbox]
        if ibox[0] <= 0:
            ibox[0] = 1
        if ibox[1] <= 0:
            ibox[1] = 1
        if ibox[2] >= w:
            ibox[2] = w-1
        if ibox[3] >= h:
            ibox[3] = h-1
        ibox.append(manned)
        face_list.append(ibox)
    return w, h, face_list
def read_xml(xml_path):
    tree = ET.parse(xml_path)  # 加载xml文档
    root = tree.getroot()  # 获取根元素
    # tag_root = root.tag  # 元素名字（格式：字符串）
    # attr_root = root.attrib  # 元素属性（格式：字典，{属性名1:属性值1, 属性名2:属性值2, 属性名3:属性值3...}）
    size = root.findall("size")[0]
    w = int(size.find("width").text)
    h = int(size.find("height").text)
    d = int(size.find("depth").text)
    face_list = []
    for obj in root.findall("object"):
        manned_name  = obj.find("manned").text
        print(obj)
        manned = int(manned_name)
        box = obj.find("bndbox")
        sbox = [box.find('xmin').text, box.find('ymin').text, box.find('xmax').text, box.find('ymax').text]
        # ibox = [box.find('xmin'), box.find('ymin'), box.find('xmax'), box.find('ymax')]
        ibox = [int(i) for i in sbox]
        if ibox[0] <= 0:
            ibox[0] = 1
        if ibox[1] <= 0:
            ibox[1] = 1
        if ibox[2] >= w:
            ibox[2] = w-1
        if ibox[3] >= h:
            ibox[3] = h-1
        ibox.append(manned)
        face_list.append(ibox)
	return w, h,d, face_list
def read_xml_ztc(xml_path):
	tree = ET.parse(xml_path)  # 加载xml文档
	root = tree.getroot()  # 获取根元素
	# tag_root = root.tag  # 元素名字（格式：字符串）
	# attr_root = root.attrib  # 元素属性（格式：字典，{属性名1:属性值1, 属性名2:属性值2, 属性名3:属性值3...}）
	size = root.findall("size")[0]
	w = int(size.find("width").text)
	h = int(size.find("height").text)
	d = int(size.find("depth").text)
	face_list = []
	for face in root.findall("object"):
		box = face.find("bndbox")
        coverflag  = face.find("cover").text
        coverflag = int(coverflag)
        sprayflag = face.find("spray").text
        sprayflag = int(sprayflag)
        sbox = [box.find('xmin').text, box.find('ymin').text, box.find('xmax').text, box.find('ymax').text]
        # ibox = [box.find('xmin'), box.find('ymin'), box.find('xmax'), box.find('ymax')]
        ibox = [int(i) for i in sbox]
        if ibox[0] <= 0:
            ibox[0] = 1
        if ibox[1] <= 0:
            ibox[1] = 1
        if ibox[2] >= w:
            ibox[2] = w-1
        if ibox[3] >= h:
            ibox[3] = h-1
        ibox.append(coverflag)
        ibox.append(sprayflag)
        face_list.append(ibox)
	return w, h, face_list
def writexml_slc(xmlname,head, bbxes, tail,respath,w,h):
    filename = respath+xmlname
    f = open(filename, "w")
    f.write(head)
    for bbx in bbxes:
        if bbx[0]<1:
            bbx[0]=1
        if bbx[1]<1:
            bbx[1]=1
        if bbx[2]<w:
            bbx[2] = w-1
        if bbx[3]<h:
            bbx[3]=h-1
        manned = bbx[4]
        if manned == 1:
            sname = 'zairen'
        elif manned == 0:
            sname = 'weizairen'
        f.write(objstr_dong % (sname,bbx[0], bbx[1], bbx[2] , bbx[3]))
    f.write(tail)
    f.close()
def mergexml():
    rootdir = 'D:/work/carPro/face/data/1214/'
    imgdir = 'D:/work/carPro/face/data/jingsaishuju/tricycle/manned1/'
    label_xml_dir = rootdir + 'slc_biaozhu_1216/mer2/'
    resdir = rootdir+'slc_biaozhu_1216/finale_merge_1216_2/'
    xmldir = 'D:/work/carPro/face/data/jingsaishuju/tricycle/xml_all/'
    train_lst = rootdir + 'train_lst_slc_1216_2.txt'
    f = open(train_lst, 'w')
    imgfiles = os.listdir(label_xml_dir)
    # xmlfiles = os.listdir(xmldir)
    for file in imgfiles:
        if file.find('.xml')!=-1:
            name = file.replace('.xml', '')
            if os.path.exists(resdir+file):
                continue
            xmlname = name + '.xml'
            label_xmlpath = label_xml_dir+xmlname
            if not os.path.exists(label_xmlpath):
                continue
            f.write(name + '\n')
            xmlpath = xmldir + xmlname
            try:
                print(name)
                print(imgdir+name+'.jpg')
                im = cv2.imread(imgdir+name+'.jpg')
            except:
                print(imgdir+name+'.jpg')
                continue
            w, h, fl = read_xml_label(label_xmlpath)
            head = headstr % (file,im.shape[1], im.shape[0], im.shape[2])
            w, h, fl2 = read_xml(xmlpath)
            for f22 in fl:
                fl2.append(f22)
            writexml_slc(xmlname,head, fl2, tailstr,resdir)

    f.close()
def drawZTCRect():
    rootdir = 'D:/work/carPro/face/data/jingsaishuju/slagcar/'
    imgdir = rootdir + 'images/'
    xmldir = rootdir + 'xml/'

    resdir = rootdir+ 'resRect_2/'
    restdir = rootdir+ 'resRect/2/2/'
    files = os.listdir(restdir)

    cnt = 0
    tnum = len(files)
    for file in files:
        cnt+=1
        if cnt % 200:
            print(tnum-cnt)
        if file.find('.jpg')!=-1:
            name = file.replace('.jpg','')
            filepath = imgdir + file
            xmlpath = xmldir + name+'.xml'
            if not os.path.exists(xmlpath) or not os.path.exists(filepath):
                print(filepath,xmlpath)
                continue
            else:
                if os.path.exists(resdir+file):
                    continue
                img = cv2.imread(filepath)
                w, h, fl = read_xml_ztc(xmlpath)
                for i in range(len(fl)):
                    box = fl[i]
                    boxw = box[2]-box[0]
                    boxh = box[3]-box[1]
                    cv2.rectangle(img, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 255, 255), 3)
                    out = str(box[4])+","+str(box[5])
                    cv2.putText(img, out, (int(box[0]), int(box[1]+boxh/3)), 2, 5, (0,255,255),6)
                cv2.imwrite(resdir+file,img)
def filterxml_lst():
    rootdir = 'D:/work/carPro/face/data/1214/1214/'
    resdir = rootdir+'filter_lst_2/'
    filepath = rootdir+'filter_slc_name_2.txt'
    xmldir = 'D:/work/carPro/face/data/jingsaishuju/tricycle/xml_all/'
    train_lst = rootdir+'train_lst_slc_2.txt'
    f = open(train_lst,'w')
    orif = open(filepath,'r')
    lines =orif.readlines()
    orif.close()
    namedic = dict()
    # xmlfiles = os.listdir(xmldir)
    for line in lines:
        file =line.strip()
        name = file.replace('.jpg','')
        if not namedic.has_key(name):
            namedic[name]=line
            xmlname = name+'.xml'
            xmlpath = xmldir+xmlname
            if os.path.exists(xmlpath):
                f.write(name + '\n')
                shutil.copy(xmlpath,resdir+xmlname)
            else:
                print(xmlpath+' is not exists')

    f.close()
def filterfaceFile():
    oriimagedir = 'D:/work/carPro/20181129_carface_3w/baoji8/pic/'
    falseimagedir = 'D:/work/carPro/20181129_carface_3w/baoji8/filter_res/filtered/6_5k/neg/'
    infolst = 'D:/work/carPro/20181129_carface_3w/baoji8/face_results.txt'
    resdir = 'D:/work/carPro/20181129_carface_3w/baoji8/filter_res/neg/'
    file = open(infolst,'r')
    neglist = resdir+'neglist_all.txt'
    resfile = open(neglist,'a')
    lines = file.readlines()
    file.close()
    files = os.listdir(falseimagedir)
    infodic = dict()
    for line in lines:
        info = line.strip().split()
        imgname = info[0]
        if not infodic.has_key(imgname):
            infodic[imgname]=line
    for f in files:
        if f.find('.jpg')!=-1:
            if infodic.has_key(f):
                info = infodic[f].strip().split()
                num = int(info[1])
                out = 'images/'+info[0]+' '+info[1]
                for i in range(num):
                    left = int(float(info[2+i*5]))
                    top = int(float(info[2 + i * 5+1]))
                    right = int(float(info[2 + i * 5+2]))
                    bottom = int(float(info[2 + i * 5+3]))
                    score = int(float(info[2 + i * 5+4])*100)
                    out = out+' '+str(left)+' '+str(top)+' '+str(right-left+1)+' '+str(bottom-top+1)+' '+str(score)
                resfile.write(out+'\n')
                oripath = oriimagedir+f
                respath = resdir+f
                shutil.copy(oripath,respath)
    resfile.close()
def filterfaceFile_true():
    oriimagedir = 'D:/work/carPro/20181129_carface_3w/baoji8/pic/'
    falseimagedir = 'D:/work/carPro/20181129_carface_3w/baoji8/filter_res/true_label/'
    infolst = 'D:/work/carPro/20181129_carface_3w/baoji8/face_results.txt'
    resdir = 'D:/work/carPro/20181129_carface_3w/baoji8/filter_res/'
    file = open(infolst,'r')
    neglist = resdir+'true_list_all.txt'
    resfile = open(neglist,'a')
    lines = file.readlines()
    file.close()
    files = os.listdir(falseimagedir)
    infodic = dict()
    for line in lines:
        info = line.strip().split()
        imgname = info[0]
        if not infodic.has_key(imgname):
            infodic[imgname]=line
    for f in files:
        if f.find('.jpg')!=-1:
            if infodic.has_key(f):
                resfile.write(infodic[f])

                # shutil.copy(oripath,respath)
    resfile.close()
def splitTxt():
    rootdir = 'D:/work/carPro/20181129_carface_3w/lable_face/'
    lstpath = rootdir+'ImageList_all.txt'
    file = open(lstpath,'r')
    lines = file.readlines()
    file.close()
    cnt = 0
    i = 1
    step = 800
    f=None
    for line in lines:
        if cnt % 600 == 0:
            if f!=None:
                f.close()
            fpath = rootdir+'ImageList_'+str(i)+'.txt'
            i+=1
            f = open(fpath,'w')
            f.write(line)
        else:
            f.write(line)
        cnt+=1
    f.close()

def xml2dong():
    rootdir = 'D:/work/carPro/face/data/1214/testxmlTrans/'
    xmldir = rootdir+'slc/'
    resdir = rootdir+'test/'

    xmlfiles = os.listdir(xmldir)
    for f in xmlfiles:
        if f.find('.xml')!=-1:
            name = f.replace('.xml', '')
            xmlpath = xmldir+f
            imgname = name+'.jpg'

            w, h, d, fl = read_xml(xmlpath)
            folder = 'pic'
            filename = imgname
            filepath = os.path.join("D:\pic",filename)
            head = headstr_dong % (folder,filename,filepath, w, h, d)
            writexml_slc(f, head, fl, tailstr, resdir,w,h)

if __name__ == '__main__':
    # filter_car_face()
    # checkFaceXML()
    # cropFace()
    # filterFace()
    # renamefile()
    # randomlist()
    # mergeLable_Anno()
    # checkRect()
    # txt2xml_face()
    # genlist()
    # xml2gth()
    # filterxml()
    # mergexml()
    # xml2dong()
