import sys

input = sys.stdin.readline
INF = 1000000001
n, m = map(int,input().split())

li = []
tr = [(-1,-1,INF,-1)]*(4*n)

def init(beg,end,node):
    """li의 beg인덱스~end인덱스(포함) 까지의 최소,최대값 저장"""

    global li, tr
    if beg == end:
        tr[node] = beg,end,li[beg],li[beg]
        return tr[node][2:]
    mid = (beg+end)//2
    mn1,mx1 = init(beg,mid,node*2)
    mn2,mx2 = init(mid+1,end,node*2+1)
    tr[node] = beg,end,min(mn1,mn2),max(mx1,mx2)
    return tr[node][2:]


def read(node,lo,hi):
    """lo인덱스~hi인덱스(포함) 중 최소,최대값 반환"""
    global li,tr
    beg,end,mn,mx = tr[node]

    if hi < beg or end < lo:return INF,-1

    if lo<= beg and end <= hi:
        return tr[node][2:]

    mn1,mx1 = read(node*2,lo,hi)
    mn2,mx2 = read(node*2+1,lo,hi)
    return min(mn1,mn2),max(mx1,mx2)
    




for _ in range(n):
    li.append(int(input()))
init(0,n-1,1)
for _ in range(m):
    a,b = map(int,input().split())
    print(*read(1,a-1,b-1))
