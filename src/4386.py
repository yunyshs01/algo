import sys
import math
input = sys.stdin.readline

n = int(input())

stars = []
edges = []
for i in range(1,n+1):
    stars.append(tuple(map(float,input().split())))
    for j in range(1,i):
        edges.append((i,j))



table = [i for i in range(n+1)]

def getId(x):
    if x == table[x]:return x
    return getId(table[x])

def mergeId(a, b):
    a = getId(a)
    b = getId(b)
    if a>b:table[a] = b
    else : table[b] = a




edges = sorted(edges,key=lambda t: ((t[0][0] - t[1][0])**2 + (t[1][0] - t[1][1])**2))

cnt = 0
cost = 0.0
for beg,end in edges:
    if getId(beg)!=getId(end):
        

