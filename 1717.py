# 1717.py

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int,input().split())
Rt = [i for i in range(n+1)]

def getRt(x):
    if Rt[x] == x:return x
    return getRt(Rt[x])

def union (a, b):
    a = getRt(a)
    b = getRt(b)
    if a == b: return
    if a>b:
        Rt[b] = a
    else : Rt[a] = b

def isFamily(a,b):
    return getRt(a) == getRt(b)
    


for ___ in range(m):
    o,a,b = map(int,input().split())
    if o==0:
        union(a,b)
    else: 
        print("YES" if isFamily(a,b) else "NO")
