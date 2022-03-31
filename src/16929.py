import sys

input = sys.stdin.readline

n, m = map(int,input().split())
li = []
visit = [[-1]*m for i in range(n)]
for __ in range(n):
    li.append(input().strip())


def dfs(y,x):
    global li,visit
    c = li[y][x]
    d = visit[y][x]
    for dy,dx in((-1,0),(0,1),(1,0),(0,-1)):
        ny = y+dy
        nx = x +dx
        if ny<0 or ny>=n or nx<0 or nx>=m:continue
        if li[ny][nx] == c and visit[ny][nx]>=1 and d - visit[ny][nx] >=3:
            return True
        if li[ny][nx] == c and visit[ny][nx]<=0:
            visit[ny][nx] = d+1
            flag = dfs(ny,nx)
            if flag:return True
            visit[ny][nx] = 0
    return False

for i in range(n):
    for j in range(m):
        if visit[i][j]!=-1:continue
        visit[i][j] = 1
        flag = dfs(i,j)
        if flag:
            print("Yes")
            exit(0)
print("No")

