import os
import shutil

def mv_file_with_name(src,xml_dst,jpg_dst):
    """
    Given directory, copy all annotated files to another directory.
    @param src:
    @param xml_dst:
    @param jpg_dst:
    @return:
    """
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

        if not os.path.exists(jpg_dst):
            os.makedirs(jpg_dst)
        if not os.path.exists(xml_dst):
            os.makedirs(xml_dst)

        jpg_dst2=os.path.join(jpg_dst,jpg)
        xml_dst2=os.path.join(xml_dst,xml)

        shutil.copy(jpg_path,jpg_dst2)
        shutil.copy(xml_path,xml_dst2)




