import sys
input = sys.stdin.readline
import math
n, m, k = map(int,input().split())

li = []
tree = [(-1,-1,0)]*(4*n)

dc = {}

def init(beg, end, node):
    global li, tree
    if (beg == end) :
        tree[node] = beg,end,li[beg]
        return tree[node][2]
    mid = (beg + end)//2
    val = init(beg,mid,node*2)+ init(mid+1,end,node*2+1)
    tree[node] = beg, end, val
    return tree[node][2]


def read(node, lo,hi):
    global li, tree
    beg,end,val = tree[node]
    if hi<beg or lo>end : return 0

    if lo<=beg and end<=hi:return val

    return read(node*2,lo,hi) +  read(node*2+1, lo,hi)


def update(node, idx, num):
    global li,tree
    beg,end,val = tree[node]
    if idx<beg or idx>end:return
    val += (num - li[idx])
    tree[node] = beg,end,val
    if beg == end : 
        li[idx] = num
        return

    update(node*2,idx,num)
    update(node*2+1,idx,num)


for _ in range(n):
    li.append(int(input()))

init(0,n-1,1)

for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a==1:
        update(1,b-1,c)
    if a == 2:
        ans = read(1,b-1,c-1)
        print(ans)