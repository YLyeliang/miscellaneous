
L = [9,1,5,8,3,7,4,6,2]
lenth=len(L)

def swap(L,i,j):
    tmp=L[j]
    L[j]=L[i]
    L[i]=tmp

def BubbleSort(L,length):
    for i in range(length):
        flag= False
        for j in range(length-1,i,-1):
            if L[j-1]>L[j]:
                swap(L,j-1,j)
                flag=True
        if not flag:
            break
    return L

L=BubbleSort(L,lenth)
print(L)