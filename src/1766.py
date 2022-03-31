# 1766.py

import sys
from queue import PriorityQueue
input = sys.stdin.readline
q = PriorityQueue()
n, m = map(int,input().split())
inDeg = [0] * (n+1)
E = [[] for i in range(n+1)]

ans = []

for ___ in range(m):
    a, b = map(int,input().split())
    E[a].append(b)
    inDeg[b]+=1

for i in range(1,n+1):
    if inDeg[i] == 0:
        q.put(i)

while not q.empty():
    now = q.get()
    ans.append(str(now))
    for d in E[now]:
        inDeg[d]-=1
        if inDeg[d] == 0:
            q.put(d)
print(' '.join(ans))


