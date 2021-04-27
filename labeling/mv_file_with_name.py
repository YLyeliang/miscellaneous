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


def mv_file_with_same_name(src,obj,dst):
    """
    Given src directory, and obj directory, all files in src having same name with ones in obj
    will be moved to dst.
    @param src:
    @param obj:
    @param dst:
    @return:
    """
    files=os.listdir(obj)
    for file in files:
        src_file=os.path.join(src,file)
        dst_file =os.path.join(dst,file)
        shutil.copy(src_file,dst_file)

def mv_file_exclude_name(src,obj,dst):
    """
    Given src directory, and obj directory, all files in src exclude ones having same name with ones in obj
    will be moved to dst
    @param src:
    @param obj:
    @param dst:
    @return:
    """
    files=os.listdir(src)
    obj_files=os.listdir(obj)
    src_files=[]
    for file in files:
        if file not in obj_files:
            src_files.append(file)
    for file in src_files:
        src_file=os.path.join(src,file)
        dst_file=os.path.join(dst,file)
        shutil.copy(src_file,dst_file)

# mv_file_exclude_name("D:\AerialGoaf\detail\\resource\\label","D:\AerialGoaf\detail\\resource\site1","D:\AerialGoaf\detail\\resource\site2label")

mv_file_with_same_name("D:\AerialGoaf\detail\\512x512\label",
                       "D:\AerialGoaf\detail\\512x512\siteB",
                       "D:\AerialGoaf\detail\\512x512\siteBlab")

