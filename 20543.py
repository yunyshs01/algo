import sys
input = sys.stdin.readline

n, m = map(int,input().split())
ter = [list(map(int,line.split())) for line in sys.stdin.readlines()]
ans = [[0] * n for i in range(n)]




for i in range(m//2,n-m//2):
    for j in range(m//2,n-m//2):
        if ter[i-m//2][j-m//2] == 0:continue
        ans[i][j] = -ter[i-m//2][j-m//2]
        

for i in range(n):
    print(' '.join(map(str,ans[i])))
