import sys

input = sys.stdin.readline

n ,m, k  = map(int,input().split())
MOD = 1000000007
li = []
for _ in range(n):
    li.append(int(input()))
tr = [0]*(4*n)
rg = [(-1,-1)]*(4*n)

def init(beg,end,node):
    rg[node] = beg,end
    if beg == end:
        tr[node] = li[beg]
        return tr[node]%MOD
    mid = (beg+end)//2
    left = init(beg,mid,node*2)%MOD
    right = init(mid+1,end,node*2+1)%MOD
    tr[node] = (left*right)%MOD

    return tr[node]%MOD

def query(node,lo,hi):
    beg,end = rg[node]
    if hi < beg or end < lo:
        return 1
    
    if lo<=beg and end<=hi:
        return tr[node]
    
    left = query(node*2,lo,hi)%MOD
    right = query(node*2+1,lo,hi)%MOD
    return (left*right)%MOD


def update(node,idx,val):
    beg,end = rg[node]
    if idx < beg or idx > end:return
    if beg == end:
        tr[node] = val%MOD
        li[idx] = val%MOD
        return 
    update(node*2,idx,val)
    update(node*2+1,idx,val)
    tr[node] = (tr[node*2]*tr[node*2+1])%MOD


init(0,n-1,1)

for __ in range(m+k):
    a,b,c  = map(int,input().split())
    if a==1:
        update(1,b-1,c)
    else:
        ans = query(1,b-1,c-1)
        print(ans)



