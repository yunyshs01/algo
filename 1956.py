import sys
input = sys.stdin.readline

v,e = map(int,input().split())

INF = 98765431
E = [[INF]*(v+1) for _ in range(v+1)]
for _ in range(e):
    a,b,w = map(int,input().split())
    E[a][b] = w


for i in range(1,v+1):
    for j in range(1,v+1):
        if i==j:E[i][j] = 0
        for k in range(1,v+1):
            if k==i or k==j :continue
            if E[i][j]>E[i][k] + E[k][j]:
                E[i][j] = E[i][k] + E[k][j]

min = INF
for i in range(1,v):
    for j in range(i+1,v+1):
        if E[i][j] + E[j][i]<min:
            min = E[i][j] + E[j][i]

print(-1 if min == INF else min)
