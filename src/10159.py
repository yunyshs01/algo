import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
mat = [[0]*n for _ in range(n)]

for __ in range(m):
    a,b = map(int,input().split())
    a-=1;b-=1
    mat[a][b] = 1
    mat[b][a] = -1


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j or k==i or k ==j :continue
            if mat[i][j]!=0:continue
            if mat[i][k] == 1 and mat[k][j] == 1:
                mat[i][j] = 1
                mat[j][i] = -1
            if mat[i][k] == -1 and mat[k][j] == -1:
                mat[i][j] = -1
                mat[j][i] = 1

for li in mat:
    print(len(list(filter(lambda x: x==0,li)))-1)



