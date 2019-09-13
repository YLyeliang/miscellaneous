N,M=[int(i) for i in input().rstrip().split()]
D=[]
for i in range(M):
    D.append(int(input().rstrip()))
print(N,M)
print(D)

# there're only 2 choices each time when decide to step D.
# Therefore,if below condition are required,then it hold.
# Start from node 1,distance = 1 + D ,after iter, keep the number,
# and remove duplicated number.

out=[]
for i in range(N):
    rr=[i]
    ll=[i]
    for j in range(M):
        right= rr[j] + D[j]
        left=ll[j]-D[j]
        if right>0 or right <=N:
            rr.append(right)
        if left >0 or left <=N:
            ll.append(left)

a=0
i=0

def get_end(start,i):
    dist=start+D[i]
    i+=1
    if dist >0 and dist <=N:
        get_end(dist,i)
    dist=start-D[i]
    if dist>0 and dist<=N:
        get_end(dist,i)
    if i==M:
        a+=1

for j in range(N):
    i=0
    get_end(j,i)

