
import sys

from copy import deepcopy

input = sys.stdin.readline

n, m = map(int,input().split())

mp = [list(map(int,input().split()))for _ in range(n)]


def bfs(y,x, mp,visit):
    global n, m
    q = [(y,x)]

    while len(q)>0:
        nowy, nowx = q[0]
        q.pop(0)
        for dy, dx in ((-1,0),(0,1),(1,0),(0,-1)):
            ny = nowy + dy
            nx = nowx + dx
            if ny<0 or ny>=n or nx<0 or nx>=m:continue
            if mp[ny][nx] == 0 and not visit[ny][nx]:
                visit[ny][nx] = True
                mp[ny][nx] = 2
                q.append((ny,nx))

def solution():
    global mp, n, m

    cp = deepcopy(mp)

    visit = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if cp[i][j] == 2 and not visit[i][j]:
                visit[i][j] = True
                bfs(i,j, cp, visit)
    ret = 0
    for li in cp:
        ret+=li.count(0)
    return ret
                


ans = -1
for i in range(n*m):
    if mp[i//m][i%m]!=0:continue
    mp[i//m][i%m] = 1
    for j in range(i+1,n*m):
        if mp[j//m][j%m]!=0:continue
        mp[j//m][j%m] = 1
        for k in range(j+1,n*m):
            if mp[k//m][k%m]!=0:continue
            mp[k//m][k%m] = 1
            ret = 0
            ret = solution()
            if ret>ans:ans = ret
            mp[k//m][k%m] = 0
        mp[j//m][j%m] = 0
    mp[i//m][i%m] = 0

print(ans)
