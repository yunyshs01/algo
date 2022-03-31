import sys,copy

input = sys.stdin.readline

n = int(input())
table  = [list(map(int,input().split()))for i in range(n)]

def left(tb):

    for i in range(n):
        done = False
        for j in range(n):
            if tb[i][j] == 0 :continue
            nx = j
            while nx>0:
                if tb[i][nx-1]!=0:
                    break
                nx -=1
            if nx == 0 or done or tb[i][nx-1] != tb[i][j]:
                temp = tb[i][j]
                tb[i][j] = 0
                tb[i][nx] = temp
                done = False
            else:
                tb[i][nx-1] *=2
                tb[i][j] = 0
                done = True
    return tb

def up(tb):

    for i in range(n):
        done = False
        for j in range(n):
            if tb[j][i] == 0 :continue
            ny = j
            while ny>0:
                if tb[ny-1][i]!=0:
                    break
                ny -=1
            if ny == 0 or done or tb[ny-1][i] != tb[j][i]:
                temp = tb[j][i]
                tb[j][i] = 0
                tb[ny][i] = temp
                done = False
            else:
                tb[ny-1][i] *=2
                tb[j][i] = 0
                done = True
    return tb

def right(tb):
    for i in range(n):
        done = False
        for j in range(n-1,-1,-1):
            if tb[i][j] == 0 :continue
            nx = j
            while nx<n-1:
                if tb[i][nx+1]!=0:
                    break
                nx +=1
            if nx == n-1 or done or tb[i][nx+1] != tb[i][j]:
                temp = tb[i][j]
                tb[i][j] = 0
                tb[i][nx] = temp
                done = False
            else:
                tb[i][nx+1] *=2
                tb[i][j] = 0
                done = True
    return tb

def down(tb):

    for i in range(n):
        done = False
        for j in range(n-1,-1,-1):
            if tb[j][i] == 0 :continue
            ny = j
            while ny<n-1:
                if tb[ny+1][i]!=0:
                    break
                ny +=1
            if ny == n-1 or done or tb[ny+1][i] != tb[j][i]:
                temp = tb[j][i]
                tb[j][i] = 0
                tb[ny][i] = temp
                done = False
            else:
                tb[ny+1][i] *=2
                tb[j][i] = 0
                done = True
    return tb

cp = copy.deepcopy

q = []

q.append((table,0))
ans = -1

while len(q):
    tb , t = q.pop()
    if t == 5:
        now =  max(map(max,tb))
        if now>ans:
            ans = now
        continue
    for fun in (up,left,down,right):
        q.append((fun(cp(tb)),t+1))

print(ans)
    
