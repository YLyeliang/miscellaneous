# def removeDuplic(N,m,arr):
#     assert N==len(arr)
#     duplicate=None
#     k=[0 for i in range(N)]
#     for i,num in enumerate(arr):
#         k[num]+=1
#     for i in k:
#         if i is not None and i >=m:
#             arr.remove()
#     return arr
#

def removeDuplic(N,m,arr):
    new_arr =set(arr)
    for i in new_arr:
        num = arr.count(i)
        if num>m:
            for j in range(num):
                arr.remove(i)
    return arr

tmp=input().split(' ')
N,m=int(tmp[0]),int(tmp[1])
arr=input().split(' ')
arr=[int(i) for i in arr]

print(removeDuplic(N,m,arr))

