import sys
input =sys.stdin.readline

n, m = map(int,input().split())

V = [(0,0) for i in range(n+1)]
E = []

R = [i for i in range(n+1)]

def getRt(x):
    if R[x] == x : return x
    return getRt(R[x])

def union (a,b):
    a = getRt(a)
    b = getRt(b)
    if a == b:return
    if a>b:R[a] = b
    else : R[b] = a

for i in range(1,n+1):
    V[i] = tuple(map(int,input().split()))

for i in range(m):
    a, b = map(int,input().split())
    
    union(a,b)
