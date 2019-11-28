import numpy as np


def g_mean1(recall,precision):
    """
    Calculate G-mean 1 metric, \sqrt (Recall * Precision)
    """
    return np.sqrt(recall*precision)

def g_mean2(recall,specificity):
    """
    Calculate G-mean 2 metric,\sqrt (Recall * Precision)
    """
    return np.sqrt(recall*specificity)

def f_score(recall,precision,beta=1,weigh_r=None,weight_p=None):
    """
    Calculate F_score metric.
    """
    if weigh_r and weight_p:
        if not weigh_r+weight_p ==1:
            raise ValueError("Recall weight + Precision weight must equal 1.")
        beta = weigh_r/weight_p
    f=(1+beta)*recall*precision/(recall+precision)
    return f

a=[99.6 ,99]
b=[95.6 ,99]
c=[71.5 , 99]
d=[70 , 99]
e=[70, 99]

print("g-mean")
print(g_mean2(*a))
print(g_mean2(*b))
print(g_mean2(*c))
print(g_mean2(*d))
print(g_mean2(*e))

print("f1-score")
# print(f_score(*a))
# print(f_score(*b))
# print(f_score(*c))
# print(f_score(*d))
# print(f_score(*e))