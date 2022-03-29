# segment tree lazy propagation
import sys
input = sys.stdin.readline

n, m, k = map(int,input().split())

li = []    #값

tr = [0] * (4*n)    #트리
lz = [0] * (4*n)    #lazy
rg = [(-1,-1)] * (4*n)#트리 노드의 범위

def init(beg,end, node):
    if beg == end:
        tr[node] = li[beg]
        rg[node] = beg,end
        return tr[node]
    mid = (beg + end)//2
    ret = init(beg,mid,node*2) + init(mid+1, end,node*2+1)
    tr[node] = ret
    rg[node] = beg,end
    return tr[node]

def propagate(node):
    if lz[node] == 0: return
    beg,end = rg[node]
    rglen = end - beg+1
    tr[node] += lz[node]*rglen
    if beg!=end:
        lz[node*2] += lz[node]
        lz[node*2+1] += lz[node]
    lz[node] = 0
    


def query(node, lo,hi):
    beg,end = rg[node]
    propagate(node)
    if hi < beg or end < lo:
        return 0
    if lo<=beg and end <= hi:
        return tr[node]
    ret = query(node*2,lo,hi) + query(node*2+1,lo,hi)
    return ret

def update(node,lo,hi,add):
    beg,end = rg[node]
    propagate(node)
    if hi < beg or end < lo:
        return
    if lo<=beg and end<=hi:
        lz[node]+=add
        propagate(node)
        return
    update(node*2,lo,hi,add)
    update(node*2+1,lo,hi,add)

    tr[node] = tr[node*2] + tr[node*2+1]
    return

for _ in range(n):
    li.append(int(input()))    
init(0,n-1,1)
for _ in range(m+k):
    q = list(map(int,input().split()))
    if q[0] == 1:
        b,c,d = q[1:]
        update(1,b-1,c-1,d)
    if q[0] == 2:
        b,c = q[1:]
        ans = query(1,b-1,c-1)
        print(ans)
    

