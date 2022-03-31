import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int,input().split()))

dp = [[0]*21 for _ in range(n)]
dp[0][num[0]] = 1
for i, dig in enumerate(num[:-1]):
    if i == 0: continue
    for j in range(21):
        if dp[i-1][j]>0:
            if j-dig>=0 : dp[i][j-dig]+=dp[i-1][j]
            if j+dig<=20 : dp[i][j+dig]+=dp[i-1][j]

print(dp[-2][num[-1]])

