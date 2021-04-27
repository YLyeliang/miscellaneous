import matplotlib.pyplot as plt
import numpy as np


# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
def bar_chart():
    # bar chart
    label=["召回率","精准率",'平均精度']
    index = np.arange(3)
    size1=[0.804,0.850,0.767]
    size2=[0.797,0.825,0.753]
    size3=[0.784,0.811,0.725]

    # data from old model.
    # recall=[0.804,0.797,0.784]
    # precision=[0.850,0.825,0.811]
    # ap=[0.767,0.753,0.725]

    # rect1=plt.bar(x=label,height=infer,width=0.4,alpha=0.8)
    # plt.xlabel("Algorithm names")
    # plt.ylabel("Inference time/ms")
    # plt.show()

    # multi sub figures in one figure
    fig=plt.figure(figsize=(12,6))
    bar1=plt.barh(y=index,height=0.2,width=size1,color='r',)
    bar2=plt.barh(y=index+0.2,height=0.2,width=size2,color='b')
    bar3=plt.barh(y=index+0.4,height=0.2,width=size3,color='g')
    for b in bar1:
        w = b.get_width()
        plt.text(w + 0.05, b.get_y() + b.get_height() / 2 , str(w), ha='center', fontsize=16)
    for b in bar2:
        w = b.get_width()
        plt.text(w + 0.05, b.get_y() + b.get_height() / 2, str(w), ha='center', fontsize=16)
    for b in bar3:
        w = b.get_width()
        plt.text(w + 0.05, b.get_y() + b.get_height() / 2, str(w), ha='center', fontsize=16)

    plt.yticks(index+0.3,label)
    plt.xlim(0,1.05)
    plt.legend(['1000x600', '800x480','600x320'], fontsize=16)
    plt.tick_params(labelsize=16)

    # for b in bar1:
    #     h=b.get_height()
    #     ax1.text(b.get_x()+b.get_width()/2,h+0.2,str(h),ha='center',va='bottom',fontsize=14)
    # plt.savefig("D:/latex_project/crack_detection_D/image/param_infer.png")
    plt.show()
    fig.savefig("size-performance.png",dpi=600)

bar_chart()