import sys
input = sys.stdin.readline

n = int(input())

mp = [list(map(int,input().split()))for _ in range(n)]
visit = [[0]*n for _ in range(n)]
cnt = 1
def bfs(y,x,h):
    global cnt, visit
    q = [(y,x)]
    visit[y][x] = cnt
    while len(q)>0:
        nowy, nowx = q[0]
        q.pop(0)
        for dy, dx in ((-1,0),(0,1), (1,0),(0,-1)):
            ny = nowy + dy
            nx = nowx + dx
            if nx<0 or nx>=n or ny<0 or ny>=n: continue
            if mp[ny][nx] > h and visit[ny][nx] == 0:
                visit[ny][nx] = cnt
                q.append((ny,nx))
    cnt+=1
ret = -1
for depth in range(100):
    cnt = 1
    visit = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if mp[i][j] >depth and visit[i][j] == 0:
                bfs(i,j,depth)
    
    if cnt>ret:ret = cnt

print(ret -1)

