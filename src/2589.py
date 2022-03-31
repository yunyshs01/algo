import sys
from collections import deque
INF = -1
input = sys.stdin.readline
n, m = map(int,input().split())
table = [[[[INF]*m for i in range(n)] for j in range(m)]for k in range(n)]
li = []
for i in range(n):
    li.append(input())

q = deque([])

dm = [(-1,0),(0,1),(1,0),(0,-1)]

for i in range(n):
    for j in range(m):
        if(li[i][j]=='W'):continue
        q.append((i,j,0))
        table[i][j][i][j] = 0
        while len(q):
            y,x,l = q.popleft()
            for dy, dx in dm:
                ny =y+dy
                nx = x + dx
                if(ny>=n or ny<0 or nx>=m or nx<0 or li[ny][nx]=='W'):continue
                if table[i][j][ny][nx]!=INF : continue
                table[i][j][ny][nx] = l+1
                table[ny][nx][i][j] = l+1
                q.append((ny,nx,l+1))

mx = -1
for  i in table:
    for j in i:
        for k in j:
            now = max(k)
            if now>mx:mx = now
print(mx)