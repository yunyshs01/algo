import sys
input = sys.stdin.readline

n, l = map(int,input().split())

mp = [list(map(int,input().split()))for _ in range(n)]

horizontal = [True]*n
vertical = [True]*n

for i in range(n):
    last = mp[i][0]
    slopeCnt = 1
    for j in range(1,l):
        if mp[i][j] != last:
            horizontal[i] = False
            break
        if slopeCnt < l: slopeCnt+=1
    if not horizontal[i]:
        continue
    
    tryDown = False
    for j in range(l,n):
        if mp[i][j] == last:
            if slopeCnt < l :
                slopeCnt+=1
            if tryDown and slopeCnt == l:
                slopeCnt = 0
                tryDown = False
        elif mp[i][j]  ==  last + 1:
            if slopeCnt == l:
                slopeCnt = 1
                last = mp[i][j]
            else:
                horizontal[i] = False
                break
        elif mp[i][j] == last - 1:
            slopeCnt = 1
            tryDown = True
            last = mp[i][j]
        else:
            horizontal[i] = False
            break
    if tryDown :horizontal[i] = False

for i in range(n):
    last = mp[0][i]
    slopeCnt = 1
    for j in range(1,l):
        if mp[j][i] != last:
            vertical[i] = False
            break
        if slopeCnt < l: slopeCnt+=1
    if not vertical[i]:
        continue
    
    tryDown = False
    for j in range(l,n):
        if mp[j][i] == last:
            if slopeCnt < l :
                slopeCnt+=1
            if tryDown and slopeCnt == l:
                slopeCnt = 0
                tryDown = False
        elif mp[j][i]  ==  last + 1:
            if slopeCnt == l:
                slopeCnt = 1
                last = mp[j][i]
            else:
                vertical[i] = False
                break
        elif mp[j][i] == last - 1:
            slopeCnt = 1
            tryDown = True
            last = mp[j][i]
        else:
            vertical[i] = False
            break
    if tryDown :vertical[i] = False


print(vertical)
print(horizontal)
print(sum(vertical) + sum(horizontal))
    
