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

lst=[]
def fn(n):
    lst.append(n if n<2 else fn(n-1)+ fn(n-2))
    print(lst)
if __name__ =='__main__':
    fn(3)
    debug=1




a = [1, 2,3,4,5 ]
b = [i for i in range(5,1,-1)]
c=a[::-1]
if a[0]<a[2]<a[1] or a[3]>a[2]>a[4]:
    print("it worked")


def removeDuplic(N, m, arr):
    new_arr = set(arr)
    for i in new_arr:
        num = arr.count(i)
        if num > m:
            for j in range(num):
                arr.remove(i)
    return arr


tmp = input().split(' ')
N, m = int(tmp[0]), int(tmp[1])
arr = input().split(' ')
arr = [int(i) for i in arr]

print(removeDuplic(N, m, arr))
