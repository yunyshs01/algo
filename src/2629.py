import sys

input = sys.stdin.readline

n = int(input())
W = list(map(int,input().split()))
m = int(input())
Q = list(map(int,input().split()))

chk = [[False]*40001 for _ in range(n)]

chk[0][W[0]] = True
for i in range(1,n):
    for j in range(40001):
        if j == W[i]:chk[i][j] = True
        if chk[i-1][j]:
            chk[i][j] = True
            if j+W[i] < 40001:chk[i][j+W[i]] = True
            if j-W[i] >=0:chk[i][j-W[i]] = True
            if W[i] - j >=0 : chk[i][W[i]-j] = True

print(' '.join(map(lambda x: 'Y'if chk[n-1][x]else 'N',Q)))

