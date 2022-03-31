
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

DRT = ((-1,0),(0,1),(1,0),(0,-1))

mp = [list(map(int,input().split())) for _ in range(n)]
ob = [[set() for i in range(m)] for j in range(n)]
def dfs(y,x):
    global n, m
    if y == n and x == 0:
        ret = 0
        for li in ob:
            ret += sum(map(lambda x: len(x) == 0,li))
        return ret
    ret = n*m
    if mp[y][x] == 1:
        for dy,dx in DRT:
            for i in range(8):
                ny = y + dy * i
                nx = x + dx * i
                if ny<0 or ny>=n or nx<0 or nx>=m:continue
                if mp[ny][nx] == 6:break
                ob[ny][nx].add((y,x))
            ans = dfs(y+(x+1)//m, (x+1)%m)
            if ans<ret : ret = ans
            for i in range(8):
                ny = y + dy * i
                nx = x + dx * i
                if ny<0 or ny>=n or nx<0 or nx>=m:continue
                if mp[ny][nx] == 6:break
                ob[ny][nx].discard((y,x))
    
    elif mp[y][x] == 2:
        for dy,dx in DRT[:2]:
            for i in range(8):
                ny = y + dy * i
                nx = x + dx * i
                if ny<0 or ny>=n or nx<0 or nx>=m:continue
                if mp[ny][nx] == 6:break
                ob[ny][nx].add((y,x))
            for i in range(8):
                ny = y - dy * i
                nx = x - dx * i
                if ny<0 or ny>=n or nx<0 or nx>=m:continue
                if mp[ny][nx] == 6:break
                ob[ny][nx].add((y,x))
            ans = dfs(y+(x+1)//m, (x+1)%m)
            if ans<ret : ret = ans
            for i in range(8):
                ny = y + dy * i
                nx = x + dx * i
                if ny<0 or ny>=n or nx<0 or nx>=m:continue
                if mp[ny][nx] == 6:break
                ob[ny][nx].discard((y,x))
            for i in range(8):
                ny = y - dy * i
                nx = x - dx * i
                if ny<0 or ny>=n or nx<0 or nx>=m:continue
                if mp[ny][nx] == 6:break
                ob[ny][nx].discard((y,x))

    elif mp[y][x] == 3:
        for (dy,dx), (dny,dnx) in zip(DRT, DRT[1:]+DRT[0:1]):
            for i in range(8):
                ny = y + dy * i
                nx = x + dx * i
                if ny<0 or ny>=n or nx<0 or nx>=m:continue
                if mp[ny][nx] == 6:break
                ob[ny][nx].add((y,x))
            for i in range(8):
                ny = y + dny * i
                nx = x + dnx * i
                if ny<0 or ny>=n or nx<0 or nx>=m:continue
                if mp[ny][nx] == 6:break
                ob[ny][nx].add((y,x))
            ans = dfs(y+(x+1)//m, (x+1)%m)
            if ans<ret : ret = ans
            for i in range(8):
                ny = y + dy * i
                nx = x + dx * i
                if ny<0 or ny>=n or nx<0 or nx>=m:continue
                if mp[ny][nx] == 6:break
                ob[ny][nx].discard((y,x))
            for i in range(8):
                ny = y + dny * i
                nx = x + dnx * i
                if ny<0 or ny>=n or nx<0 or nx>=m:continue
                if mp[ny][nx] == 6:break
                ob[ny][nx].discard((y,x))
    
    elif mp[y][x] == 4:
        for (dy,dx), (dny,dnx), (dnny,dnnx) in zip(DRT, DRT[1:]+DRT[0:1], DRT[2:] + DRT[:2]):
            for i in range(8):
                ny = y + dy * i
                nx = x + dx * i
                if ny<0 or ny>=n or nx<0 or nx>=m:continue
                if mp[ny][nx] == 6:break
                ob[ny][nx].add((y,x))
            for i in range(8):
                ny = y + dny * i
                nx = x + dnx * i
                if ny<0 or ny>=n or nx<0 or nx>=m:continue
                if mp[ny][nx] == 6:break
                ob[ny][nx].add((y,x))
            for i in range(8):
                ny = y + dnny * i
                nx = x + dnnx * i
                if ny<0 or ny>=n or nx<0 or nx>=m:continue
                if mp[ny][nx] == 6:break
                ob[ny][nx].add((y,x))
            ans = dfs(y+(x+1)//m, (x+1)%m)
            if ans<ret : ret = ans
            for i in range(8):
                ny = y + dy * i
                nx = x + dx * i
                if ny<0 or ny>=n or nx<0 or nx>=m:continue
                if mp[ny][nx] == 6:break
                ob[ny][nx].discard((y,x))
            for i in range(8):
                ny = y + dny * i
                nx = x + dnx * i
                if ny<0 or ny>=n or nx<0 or nx>=m:continue
                if mp[ny][nx] == 6:break
                ob[ny][nx].discard((y,x))
            for i in range(8):
                ny = y + dnny * i
                nx = x + dnnx * i
                if ny<0 or ny>=n or nx<0 or nx>=m:continue
                if mp[ny][nx] == 6:break
                ob[ny][nx].discard((y,x))
    elif mp[y][x] == 5:
        for dy,dx in DRT:
            for i in range(8):
                ny = y + dy * i
                nx = x + dx * i
                if ny<0 or ny>=n or nx<0 or nx>=m:continue
                if mp[ny][nx] == 6:break
                ob[ny][nx].add((y,x))
        ans = dfs(y+(x+1)//m, (x+1)%m)
        if ans<ret : ret = ans
        for dy,dx in DRT:
            for i in range(8):
                ny = y + dy * i
                nx = x + dx * i
                if ny<0 or ny>=n or nx<0 or nx>=m:continue
                if mp[ny][nx] == 6:break
                ob[ny][nx].discard((y,x))
    else:
        if mp[y][x] == 6:
            ob[y][x].add((y,x))
        ans = dfs(y+(x+1)//m, (x+1)%m)
        if ans<ret : ret = ans
    
    
    return ret

print(dfs(0,0))

