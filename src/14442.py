"""
Solved
20200405
14442.py
벽 부수고 이동하기 2
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int,input().split())
li = []
for _ in range(n):
    li.append(list(map(int,input().strip())))


q = deque([])
q.append((0,0,0,0)) # y, x, broken walls, path length
visit = [[-1]*m for _ in range(n)]
visit[0][0] = 0
ans = -1
while q:
    y,x,b,t = q[0]
    q.popleft()
    if y == n-1 and x == m-1:
        ans = t+1
        break

    for dy,dx in zip((-1,1,0,0),(0,0,-1,1)):
        ny = y + dy
        nx = x + dx
        if ny<0 or ny>=n or nx<0 or nx>=m:continue
        if li[ny][nx] == 1 and b <k and (visit[ny][nx]==-1 or visit[ny][nx] > b+1) :
            visit[ny][nx] = b+1
            q.append((ny,nx,b+1,t+1))
        elif li[ny][nx] == 0 and (visit[ny][nx]==-1 or visit[ny][nx] > b):
            visit[ny][nx] = b
            q.append((ny,nx,b,t+1))
print(ans)

