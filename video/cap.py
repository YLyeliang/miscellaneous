array,pi=input().replace(' ','').split(',')
array=list(map(int,array.split('->')))
pi=int(pi)

left=[]
right=[]
mid=[]
for i in array:
    if i<pi:
        left.append(i)
    elif i==pi:
        mid.append(i)
    else:
        right.append(i)

res=list(map(str,left+mid+right))
out="->".join(res)
print(out)