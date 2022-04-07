"""
Solved
20200407
14391.py
종이 조각
"""
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

li = [list(map(int,input().strip()))for _ in range(n)]
cn = [[0]*m for _ in range(n)]

def dfs(pos):
    y,x = divmod(pos,m)

    if pos==n*m:
        ret = 0
        visit = [[False]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if visit[i][j]:continue
                visit[i][j] = True
                now = li[i][j]
                ni,nj = i,j
                while cn[ni][nj]!=0:
                    if cn[ni][nj]==1:
                        nj+=1
                        now=now*10 + li[ni][nj]
                        visit[ni][nj] = True
                    elif cn[ni][nj] == -1:
                        ni+=1
                        now = now*10 + li[ni][nj]
                        visit[ni][nj] = True
                ret+=now

    ret = 0

    if (y>0 and cn[y-1][x] == -1) and (x>0 and cn[y][x-1] == 1):
        return 0
    
    if x < m-1 and not(y>0 and cn[y-1][x] == -1):
        cn[y][x] = 1
        now = dfs(pos+1)
        if now>ret:ret = now
        cn[y][x]= 0
    if y < n-1 and not(x>0 and cn[y][x-1] == 1):
        cn[y][x] = -1
        now = dfs(pos+1)
        if now>ret:ret = now
        cn[y][x] = 0
    

    now = dfs(pos+1)
    if now>ret:ret = now

    return ret

print(dfs(0))