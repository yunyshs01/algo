import sys
input =sys.stdin.readline

test_case = 1



def cd(st):
    return ord(st[0])-ord('A'), int(st[1])-1

def putable(y,x,num):
    global li
    for i in range(9):
        if i == x:continue
        if num == li[y][i]:
            return False
    for i in range(9):
        if i == y:continue
        if num == li[i][x]:
            return False
    for i in range(3):
        for j in range(3):
            ni = i+(y//3)*3
            nj = j+(x//3)*3
            if ni==y and nj == x:continue
            if num == li[ni][nj]:
                return False
    return True
def dfs(coord):
    global li,n, visit
    y,x = divmod(coord,9)
    if y == 9 and x == 0:
        return True
    if li[y][x]!=0:
        return dfs(coord+1)

    for key in visit:
        if visit[key]:continue

        ok = putable(y,x,key[0]), putable(y,x,key[1])
        if not any(ok):continue

        #horizontal
        if x<8 and li[y][x+1]==0 :
            # ascending
            if  ok[0] and putable(y,x+1,key[1]):
                li[y][x] = key[0]
                li[y][x+1] = key[1]
                visit[key] = True
                if dfs(coord+1):return True
                visit[key] = False
                li[y][x+1] = 0
                li[y][x] = 0
            # descending
            if ok[1] and putable(y,x+1,key[0]):
                li[y][x] = key[1]
                li[y][x+1] = key[0]
                visit[key] = True
                if dfs(coord+1):return True
                visit[key] = False
                li[y][x+1] = 0
                li[y][x] = 0
        # vertical
        if y<8 and li[y+1][x]==0 :
            # ascending
            if ok[0] and putable(y+1,x,key[1]):
                li[y][x] = key[0]
                li[y+1][x] = key[1]
                visit[key] = True
                if dfs(coord+1):return True
                visit[key] = False
                li[y+1][x] = 0
                li[y][x] = 0
            # descending
            if ok[1] and putable(y+1,x,key[0]):
                li[y][x] = key[1]
                li[y+1][x] = key[0]
                visit[key] = True
                if dfs(coord+1):return True
                visit[key] = False
                li[y+1][x] = 0
                li[y][x] = 0
    return False
            



while True:
    n = int(input())
    if n==0:break
    li = [[0] * 9 for _ in range(9)]
    visit = {(i,j) : False for i in range(1,9) for j in range(i+1,10)}
    for _ in range(n):
        a,b,c,d = input().split()
        a = int(a)
        b = cd(b)
        c = int(c)
        d = cd(d)
        li[b[0]][b[1]] = a
        li[d[0]][d[1]] = c
        visit[((a,c)if a <c else (c,a))] = True
        
    for i, st in enumerate(input().split()):
        y,x = cd(st)
        li[y][x] = i+1
    
    if not dfs(0):raise
    print(f'Puzzle {test_case}')
    for st in li:
        print(''.join(map(str,st)))

    test_case+=1