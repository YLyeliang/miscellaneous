
def readint():
    tmp=[int(i) for i in input().strip().split()]
    return tmp

n=input()
equa=input().split(' ')
numbers=[str(i) for i in range(10)]
ops=['+','-','*','/']
nums=[]

def comp(a,b):
    if a <=b:
        return a
    else:return b

# 对所有数字进行优先级标记，如果是乘或者除，则两边数字优先级最高，算一个类别，可以排序
# 对减号后面的数字归为一类，如果该类别优先级低于乘，则保留乘法优先级
# 对 加号 前面数字归为一类。最后对同一类别的数字进行排序
for i in range(len(equa)):
    if equa[i] in ops:
        continue
    nums.append(int(equa[i]))

flags=[3 for i in range(len(nums))]
j=0
for i in range(1,len(equa),2):
    if equa[i] =='+':
        flags[j] = comp(3, flags[j])
    if equa[i] =='-':
        flags[j+1] =comp(2,flags[j+1])
    if equa[i] == '*':
        flags[j]=comp(1,flags[j])
        if equa[i-2] =='/' or equa[i+2] =='/':
            flags[j]=comp(0,flags[j])
    if equa[i] =='/':
        flags[j]=comp(0,flags[j])
        flags[j+1]=comp(0,flags[j])
    j+=1





# for i in range(1,len(equa),2):
#     j=0
#     if equa[i] == '+':
#         flags[j]=comp(3,flags[j])
#     if equa[i] == '-':
#         flags[j+1]=comp(2,flags[j])
#     if equa[i] == '*':
#         flags[j]=comp(1,flags[j])
#         flags[j+1]=comp(1,flags[j+1])
#     if equa[i] =='/':
#         flags[j+1]=comp(1,flags[j])
#     j+=1


debug=1