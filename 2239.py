import sys
input = sys.stdin.readline

mp = [input() for _ in range(9)]
mp = list(map(lambda x: list(map(int,list(x.strip()))), mp))

horizontal = [[False]*10 for _ in range(9)]
vertical = [[False]*10 for _ in range(9)]
box = [[False]*10 for _ in range(9)]

cnt = 81

for i in range(9):
    for j in range(9):
        if mp[i][j]!=0:
            horizontal[i][mp[i][j]] = True
            vertical[j][mp[i][j]] = True
            box[(i//3)*3 + (j//3)][mp[i][j]] = True
            cnt-=1


def dfs(y,x):
    global cnt
    if mp[y][x]!=0:
        return dfs(y + (x+1)//9,(x+1)%9)
    for i in range(1,10):
        if horizontal[y][i] or vertical[x][i] or box[(y//3)*3 + (j//3)][i]:
            continue

        mp[y][x] = i
        horizontal[y][i] = True
        vertical[x][i] = True
        box[(y//3)*3 + (j//3)][i] = True
        cnt-=1
        if cnt == 0 : return True
        if dfs(y + (x+1)//9,(x+1)%9):return True
        mp[y][x] = 0
        horizontal[y][i] = False
        vertical[x][i] = False
        box[(y//3)*3 + (j//3)][i] = False
        cnt+=1

dfs(0,0)
print('\n'.join(map(lambda x: ''.join(map(str,x)),mp)))
        

