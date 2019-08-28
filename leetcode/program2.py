import sys
import numpy as np

# 健身
# Input
n = int(sys.stdin.readline().strip())
# n=5
values = []
# values=[[1,2,3,4,5],[1,1,1,1,1]]
for i in range(2):
    line = sys.stdin.readline().strip()
    values.append(list(map(int, line.split())))

X=values[0]
E=values[1]
del values

def maximumEffect(n, X, E):
    maxeffects = []
    effect_tmp=[2*X[i]+E[i] for i in range(n)]
    X=np.array(X)
    E=np.array(E)
    # index=np.argsort(effect_tmp)[::-1]
    index=[]
    for i in range(1,n+1):
        e=2*np.max(X[index[:i]])+np.sum(E[index[:i]])
        maxeffects.append(e)
    return maxeffects
maxE=maximumEffect(n,X,E)

# Output
for i in range(n):
    print(maxE[i])

# 解一元一次方程
# def s(eq, var='X'):
#     r = eval(eq.replace('=', '-(') + ')', {var:1j})
#     if r.imag ==0:
#         return -1
#     return int(-r.real / r.imag)
# equa=sys.stdin.readline().strip()
# print(s(equa))

#无重复字符最长子串
# def Unique_Str(s):
#     res_list = []
#     length = len(s)
#     for i in range(length):
#         tmp = s[i]
#         for j in range(i + 1, length):
#             if s[j] not in tmp:
#                 tmp += s[j]
#             else:
#                 break
#         res_list.append(tmp)
#     for i in range(len(res_list)):
#         k = i
#         j = i + 1
#         while j < len(res_list):
#             if len(res_list[k]) > len(res_list[j]):
#                 k = j
#             j += 1
#         if i != k:
#             res_list[i], res_list[k] = res_list[k], res_list[i]
#     return res_list[-1]
#
# char = input()
# result = Unique_Str(char)
# print(len(result))