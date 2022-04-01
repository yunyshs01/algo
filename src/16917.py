"""
Solved
20220401
16197.py
두 동전
"""

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int,input().split())
li =[list(input().strip()) for _ in range(n)]

coins = []
for i, st in enumerate(li):
    while True:
        try:
            j = st.index('o')
            li[i][j] = '.'
            coins.append((i,j))
        except ValueError:
            break

q = deque([(tuple(coins),0)])
ans = -1
visit = defaultdict(bool)
visit[q[0][0]] = True
while q:
    ((y1,x1),(y2,x2)),t =q[0]
    q.popleft()
    if t == 10:
        ans = -1
        break
    flag = False
    for dy,dx in zip((-1,0,1,0),(0,1,0,-1)):
        ny1 = y1 + dy
        nx1 = x1 + dx
        ny2 = y2 + dy
        nx2 = x2 + dx
            
        if  (ny2>=n or ny2<0 or nx2<0 or nx2>=m) and (ny1>=n or ny1<0 or nx1<0 or nx1>=m):
            continue
        if (ny2>=n or ny2<0 or nx2<0 or nx2>=m) or (ny1>=n or ny1<0 or nx1<0 or nx1>=m):
            flag = True
            break
        if li[ny2][nx2] == '#':
            ny2-=dy
            nx2-=dx
        if li[ny1][nx1] == '#':
            ny1-=dy
            nx1-=dx
        if visit[((ny2,nx2),(ny1,nx1))]or visit[((ny1,nx1),(ny2,nx2))]:
            continue
        
        visit[((ny2,nx2),(ny1,nx1))] = True
        q.append((((ny1,nx1),(ny2,nx2)),t+1))
    if flag:
        ans = t+1
        break

print(ans)
