import sys
input = sys.stdin.readline

n, m = map(int,input().split())
li = []
for __ in range(n):
    li.append(list(map(int,input().split())))

subsum = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        left = 0
        up = 0
        diag = 0
        if j>0:left = subsum[i][j-1]
        if i>0:up = subsum[i-1][j]
        if i>0 and j>0:diag = subsum[i-1][j-1]
        subsum[i][j] = left + up - diag + li[i][j]

#print(subsum)
for __ in range(m):
    x1,y1,x2,y2 = map(lambda x: int(x)-1,input().split())
    left = 0
    up = 0
    diag = 0
    if y1>0:left = subsum[x2][y1-1]
    if x1>0:up = subsum[x1-1][y2]
    if y1>0 and x1>0:diag = subsum[x1-1][y1-1]
    #print(f'{subsum[x2][y1]} - {left} - {up} + {diag}')
    print(subsum[x2][y2] - left - up + diag)



