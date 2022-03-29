
import sys
input = sys.stdin.readline

n = int(input())

table = []
atk = [[0]*n for _ in range(n)]

dyx = ((-1,1),(1,1),(1,-1),(-1,-1))

for __ in range(n):
    table.append(list(map(int,input().split())))


def dfs(cdnum):
    global n, table,atk
    y,x = divmod(cdnum,n)
    if cdnum == n*n:
        return 0
    ret = 0
    if table[y][x] == 1 and atk[y][x]==0:
        atk[y][x]+=1
        for dy,dx in dyx:
            for i in range(1,n):
                ny = y + dy*i
                nx = x + dx*i
                if ny<0 or ny>=n or nx<0 or nx>=n:continue
                atk[ny][nx]+=1
        table[y][x] = 2
        now = dfs(cdnum+1) + 1
        table[y][x] = 1
        atk[y][x]-=1
        for dy,dx in dyx:
            for i in range(1,n):
                ny = y + dy*i
                nx = x + dx*i
                if ny<0 or ny>=n or nx<0 or nx>=n:continue
                atk[ny][nx]-=1
        if now > ret:ret = now
    
    now = dfs(cdnum+1)
    if now>ret:ret = now

    return ret
    

print(dfs(0))