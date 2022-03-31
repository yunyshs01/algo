#1238.py

from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = 98765431

n, m, x = map(int,input().split())

E = [[]for _ in range(n)]
D = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int,input().split())
    E[a-1].append((b-1, c))

def dijkstra(b):
    global n, m, E, D
    adj = []
    visit = [0]*n
    visit[b] = True
    for v, w in E[b]:
        heappush(adj,(w,v))
    
    while adj:
        dist, v = heappop(adj)
        if visit[v]:continue
        visit[v]  = True
        D[b][v] = dist
        for nv,nw in E[v]:
            if visit[nv]:continue
            heappush(adj,(dist + nw,nv))
        


    

mx = -1

for i in range(n):
    dijkstra(i)
for i in range(n):
    now = D[i][x-1] + D[x-1][i]
    if now>mx :mx = now
    

print(mx)

