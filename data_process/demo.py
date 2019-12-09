from data_process.data_prepare import *
from data_process.crop import Random_crop



# 文件重命名
# path = "D:\\zmhj_photo\\det_img"
# dst_path = "D:\\zmhj_photo\\det_img"
# filesrename(path,dst_path,prefix='0',postfix='jpg')
# cvtImgs(path,dst_path,dsize=(1536,1024))



images_path = "D:\\zmhj_photo\\det_img\\labelled\\img"
annots_path = "D:\\zmhj_photo\\det_img\\labelled\\xml"
# xml_path = "D:/data/stitch/Annotations/Line12_up_20190128023906_91_0km+968.1m_forward.xml"
out_xml = "D:\\zmhj_photo\\det_img\\cropped\\Annotations"
out_crop = "D:\\zmhj_photo\\det_img\\cropped\\JPEGImages"


Crop_net = Random_crop(images_path, annots_path,
                       out_xml, out_crop,crop_width=800,crop_height=600,crop_time=500,dist_cond=80)
Crop_net.random_crop()