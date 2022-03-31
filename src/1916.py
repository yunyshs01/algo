#20220323
#1916.py

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
m = int(input())
E = [[]for _ in range(n)]
D = [0]*n
for _ in range(m):
    a,b,c = map(int,input().split())
    E[a-1].append((b-1,c))

beg,end = map(int,input().split())

visit = [False]*n

visit[beg-1] = True
adj = []
for nv, nw in E[beg-1]:
    heappush(adj,(nw,nv))

while adj:
    dist, v = heappop(adj)
    if visit[v] : continue
    visit[v] = True
    D[v] = dist
    for nv, nw in E[v]:
        if visit[nv]:continue
        heappush(adj,(dist+nw,nv))

print(D[end-1])
