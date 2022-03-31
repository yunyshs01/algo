import enum
import sys
input = sys.stdin.readline

n, m, h = map(int,input().split())

li = [[False]*(n + 2) for _ in range(h)]

for _ in range(m):
    a, b = map(int,input().split())
    li[a-1][b] = True
   


def chk(li):
    global n, m, h
    
    for i in range(1,n):
        now = i
        for j in range(h):
            if li[j][now]:now+=1
            elif li[j][now-1]:now-=1
        if now!=i : return False
    return True
    





def dfs(num, li, put):
    global n, m, h
    if num == n*h:
        if chk(li):
            return put
        return 4
    y, x = divmod(num, n)
    x+=1
    ret = 4
    if put <3 and not li[y][x] and not li[y][x-1] and not li[y][x+1]:
        li[y][x] = True
        ans = dfs(num+1,li,put+1)
        if ans < ret: ret = ans
        li[y][x] = False
    ans = dfs(num+1,li, put)
    if ans <ret : ret = ans
    return ret


ans  = dfs(0,li,0)
print(-1 if ans == 4 else ans)
