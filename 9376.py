import sys
input = sys.stdin.readline

dyx = ((-1,0),(0,1),(1,0),(0,-1))



def getRoot(x):
    global wSet
    if wSet[x] == x:return x
    return getRoot(wSet[x])

def union(a,b):
    global wSet
    a = getRoot(a)
    b = getRoot(b)
    if a == b:
        return
    if a > b: a,b = b,a
    wSet[b] = a

def isFamily(a,b):
    return getRoot(a) == getRoot(b)

t = int(input())
for ____ in range(t):
    h, w = map(int,input().split())
    mat = []
    for _ in range(h):
        mat.append(list(input().strip()))
    ok = {'exit':False, 'friend':False}
    visit = [[-1]*w for _ in range(h)]
    psr = []
    wSet = [0]
    wyx = {0:psr[0]}
    for i, li in enumerate(mat):
        while True:
            try:
                j = li.index('$')
                li[j] = '.'
                psr.append((i,j))
            except :
                break
    nwid = 1
    wq = [0]
    q = []
    

    while wq:
        nowWall = wq.pop(0)
        wy,yx = wyx[nowWall]
        while q:
            y,x = q.pop(0)

            for dy, dx in dyx:
                ny = y + dy
                nx = x + dx
                if ny<0 or ny>=h or nx<0 or nx>=w:
                    ok['exit'] = True
                    if all(ok.values()):
                        #TO-DO
                        exit()
                if mat[ny][nx] == '.' and visit[ny][nx] == -1:
                    q.append(ny,nx)
                    visit[ny][nx] = nowWall
                if mat[ny][nx] == '#' and visit[ny][nx] == -1:
                    wq.append(nwid)
                    visit[ny][nx] = nwid
                    wyx[nwid] = ny,nx
                    wSet.append(nwid)
                    nwid+=1
                if mat[ny][nx] == '#' and visit[ny][nx]!=-1 and visit[ny][nx]!=nowWall:
                    union(nowWall,visit[ny][nx])

                if visit[ny][nx]!=nowWall




    



    
