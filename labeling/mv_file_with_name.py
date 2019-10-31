import os
import shutil



def mv_file_with_name(src,xml_dst,jpg_dst):
    files=os.listdir(src)
    xmls=[]
    for i in files:
        if 'xml' in i:
            xmls.append(i)
    xmls.sort()
    for xml in xmls:
        jpg=xml[:-3]+'jpg'
        jpg_path=os.path.join(src,jpg)
        xml_path=os.path.join(src,xml)

        jpg_dst=os.path.join(jpg_dst,jpg)
        xml_dst=os.path.join(xml_dst,xml)
        shutil.copy(jpg_path,jpg_dst)
        shutil.copy(xml_path,xml_dst)

for i in range(1,8):
    yes_path="/data2/yeliang/py_project/leak_water_detect/data/20190929/line8/Camera{}_yes".format(i)
    no_path = "/data2/yeliang/py_project/leak_water_detect/data/20190929/line8/Camera{}_no".format(i)
    xml_dst='/data2/yeliang/py_project/leak_water_detect/data/20190929/Annotations'
    jpg_dst='/data2/yeliang/py_project/leak_water_detect/data/20190929/JPEGImages'
    mv_file_with_name(yes_path,xml_dst,jpg_dst)
    mv_file_with_name(no_path,xml_dst,jpg_dst)

