import matplotlib.pyplot as plt
import pandas as pd

# line chart
def line_chart():
    df = pd.read_csv("D:/latex_project/multi_input_dense_0.01.csv")
    data =df.values
    msi_loss=[]
    ss_loss=[]
    for row in data:
        msi_loss.append(row[2])
        ss_loss.append(row[5])

    step=[100*i for i in range(len(msi_loss))]
    fig=plt.figure(figsize=(9,6))
    plt.plot(step,msi_loss,c='red',label="training set A")
    plt.plot(step,ss_loss,c='blue',label="training set B")
    plt.tick_params(labelsize=16)
    plt.tick_params(labelsize=16)
    plt.ylim(0,0.7)
    # plt.xticks(range(0,50001,10000))
    # plt.yticks()

    plt.xlabel("Iterations",fontsize=16)
    plt.ylabel("loss",fontsize=16)
    plt.legend()
    plt.savefig("D:/latex_project/crack_detection_D/image/loss_map.png")
    plt.show()

line_chart()

def bar_chart():
    # bar chart
    label=["MSI-FCN","FCD-56",'FCN-16']
    infer=[26,18,40]

    param=[2.2,1.9,39]

    # rect1=plt.bar(x=label,height=infer,width=0.4,alpha=0.8)
    # plt.xlabel("Algorithm names")
    # plt.ylabel("Inference time/ms")
    # plt.show()

    # multi sub figures in one figure
    fig=plt.figure(figsize=(12,6))
    ax1=fig.add_subplot(1,2,1)
    ax2=fig.add_subplot(1,2,2)
    bar1=ax1.bar(x=label,height=infer,width=0.4)
    for b in bar1:
        h=b.get_height()
        ax1.text(b.get_x()+b.get_width()/2,h+0.2,str(h),ha='center',va='bottom',fontsize=14)
    ax1.set_xlabel("Algorithm names",fontsize=16)
    ax1.set_ylabel("Inference time/ms",fontsize=16)
    bar2=ax2.bar(x=label,height=param,width=0.4,alpha=0.8,color='green')
    for b in bar2:
        h=b.get_height()
        ax2.text(b.get_x()+b.get_width()/2,h+0.2,str(h),ha='center',va='bottom',fontsize=14)
    ax2.set_xlabel("Algorithm names",fontsize=16)
    ax2.set_ylabel("Parameters/M",fontsize=16)
    ax1.tick_params(labelsize=16)
    ax2.tick_params(labelsize=16)
    plt.savefig("D:/latex_project/crack_detection_D/image/param_infer.png")
    plt.show()




