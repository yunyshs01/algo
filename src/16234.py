
import sys
input = sys.stdin.readline

n, l, r = map(int,input().split())

mp = [list(map(int,input().split())) for _ in range(n)]




def getRoot(y, x):
    global un
    if un[y][x] == (y,x):
        return (y,x)
    return getRoot(*un[y][x])

def union(y1,x1,y2,x2):
    global sets, un
    a = getRoot(y1,x1)
    b = getRoot(y2,x2)

    if a == b: return

    if a > b:
        a,b = b,a
    try:
        sets[a]
    except KeyError:
        sets[a] = set()
        sets[a].add(a)
    
    try:
        sets[b]
    except KeyError:
        sets[b] = set()
        sets[b].add(b)
    
    un[b[0]][b[1]] = un[a[0]][a[1]]
    sets[a] |=sets[b]
    del sets[b]


def flatten(nations):

    pops = sum(map(lambda x : mp[x[0]][x[1]],nations)) // len(nations)
    for y, x in nations:
        mp[y][x] = pops


for ans in range(2000):
    moved = False
    sets = {}
    un = [[(i,j) for j in range(n)]for i in range(n)]
    for i in range(n):
        for j in range(n):
            if j < n-1:
                diff = abs(mp[i][j] - mp[i][j+1])
                if diff >=l and diff <= r:
                    union(i,j,i,j+1)
                    moved = True
            if i < n-1 :
                diff = abs(mp[i][j] - mp[i+1][j])
                if diff >=l and diff <= r:
                    union(i,j,i+1,j)
                    moved = True
    for nations in sets.values():
        flatten(nations)

    if not moved:
        print(ans)
        break
else:
    print('fail')
    
