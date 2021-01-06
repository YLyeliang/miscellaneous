import json
import six
import os
import matplotlib.pyplot as plt
import seaborn as sns

# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

root = 'D:/tmp/mmdet_crack/goaf'

path = "D:/tmp/mmdet_crack/goaf/cascade_rcnn_r50_fpn_1x_crack/20191211_161628.log.json"

dirs_ = os.listdir(root)
dirs = []
# keeps the goaf directories.
for dir in dirs_:
    if os.path.isdir(os.path.join(root, dir)) and 'goaf' in dir:
        dirs.append(os.path.join(root, dir))


def read_json_from_dir(dir):
    def read_json(json_path):
        if 'cascade' in json_path:
            with open(json_path) as f:
                cls_loss = []
                reg_loss = []
                for i in f:
                    setting = json.loads(i)
                    iter = setting['iter']
                    cls = setting['s0.loss_cls'] + setting['s1.loss_cls'] + setting['s2.loss_cls']
                    reg = setting['s0.loss_bbox'] + setting['s1.loss_bbox'] + setting['s2.loss_bbox']
                    loss = setting['loss']
                    cls_loss.append(cls)
                    reg_loss.append(reg)

        else:
            with open(json_path) as f:
                cls_loss = []
                reg_loss = []
                for i in f:
                    setting = json.loads(i)
                    iter = setting['iter']
                    cls = setting['loss_cls']
                    reg = setting['loss_bbox']
                    loss = setting['loss']
                    cls_loss.append(cls)
                    reg_loss.append(reg)
        return cls_loss, reg_loss

    files = os.listdir(dir)
    for file in files:
        if 'json' in file:
            json_file = os.path.join(dir, file)
            break
    return read_json(json_file)


# def line_chart(losses):
#     step=[100*i for i in range(len(msi_loss))]
#     fig=plt.figure(figsize=(9,6),dpi=256)
#     plt.plot(step,msi_loss,c='red',label="training set A")
#     # plt.tick_params(labelsize=18)
#     plt.plot(step,ss_loss,c='blue',label="training set B")
#     plt.tick_params(labelsize=18)
#     plt.ylim(0,0.7)
#     # plt.xticks(range(0,50001,10000))
#     # plt.yticks()
#     plt.xlabel("Iterations",fontsize=18)
#     plt.ylabel("loss",fontsize=18)
#     plt.legend(['training set A','training set B'],fontsize=16)
#     plt.show()


dirs = [dirs[0]] + [dirs[2]] + dirs[4:]
dirs[2], dirs[3], dirs[4], dirs[5] = dirs[-2], dirs[-1], dirs[2], dirs[3]
names = ['Cascade R-CNN', 'Faster R-CNN', '本文算法', 'RetinaNet', 'SSD300', 'SSD512']
names[2], names[3], names[4], names[5] = names[-2], names[-1], names[3], names[2]
color = ['red', 'green', 'orange', 'darkviolet', 'deeppink', 'cyan']
losses = {}
length = []
for i, dir in enumerate(dirs):
    name = names[i]
    cls_loss, reg_loss = read_json_from_dir(dir)
    losses[name] = [cls_loss, reg_loss]
    length.append(len(cls_loss))

step = [50 * i for i in range(min(length))]
fig = plt.figure(figsize=(9, 6), dpi=600)
for i, key in enumerate(losses):
    plt.plot(step, losses[key][0][:min(length)], c=color[i], label=key)  # 1 means reg loss, 0 means cls loss.
    # plt.tick_params(labelsize=18)
    # plt.plot(step,ss_loss,c='blue',label="training set B")
    plt.tick_params(labelsize=18)
    plt.ylim(0, 5)
    # plt.xticks(range(0,50001,10000))
    # plt.yticks()
# plt.xlabel("Iterations",fontsize=18)
plt.xlabel("本文算法", fontsize=18)
# plt.ylabel("Classification loss",fontsize=18)
plt.ylabel("分类损失", fontsize=18)
# plt.ylabel("Regression loss",fontsize=18)
plt.legend(names, fontsize=16)
plt.show()
fig.savefig("cls-loss.png", dpi=300) # cls-loss.pdf

debug = 1
