
import sys
input = sys.stdin.readline

Fset = frozenset

r, c = map(int,input().split())
mp = [list(input().rstrip())for _ in range(r)]

sets = {}
for i in range(r):
    for j in range(c):
        sets[(i,j)] = (i,j)

def getSet(cd):
    if sets[cd] == cd:
        return cd
    return getSet(sets[cd])

def union (y1,x1,y2,x2):
    a = getSet((y1,x1))
    b = getSet((y2,x2))
    if a==b :return
    if a<=b:
        sets[b] = a
    else:
        sets[a] = b
    

ducks = []

adj = {}

for i, li in enumerate(mp):
    try:
        j = li.index('L')
        ducks.append((i,j))
        li[j] = '.'
    except:
        pass


def bfs(y,x):
    global r,c
    q= [(y,x)]
    
    while len(q)>0:
        nowy, nowx = q[0]
        q.pop(0)
        for dy, dx  in((-1,0),(0,1),(1,0),(0,-1)):
            ny = nowy + dy
            nx = nowx + dx
            if ny<0 or ny>=r or nx<0 or nx>=c:
                continue
            if mp[ny][nx] == '.' and getSet((ny,nx)) == (ny,nx):
                union(nowy,nowx,ny,nx)
                q.append((ny,nx))
            elif mp[ny][nx] == 'X':
                adj[(ny,nx)] = (nowy,nowx)
    


for i in range(r):
    for j in range(c):
        if mp[i][j] == '.' and getSet((i,j)) == (i,j):
            bfs(i,j)

for ret in range(1,1500):
    newadj = {}
    for (nowy, nowx)in adj:
        mp[nowy][nowx] = '.'
        for dy, dx  in((-1,0),(0,1),(1,0),(0,-1)):
            ny = nowy + dy
            nx = nowx + dx
            if ny<0 or ny>=r or nx<0 or nx>=c:
                continue
            if mp[ny][nx] == 'X':
                newadj[(ny,nx)] = (nowy,nowx)
            elif mp[ny][nx] == '.':
                union(nowy,nowx,ny,nx)
    adj = newadj
    
    if getSet(ducks[0]) is getSet(ducks[1]):
        print(ret)
        break
else:
    print('Fail')
        





