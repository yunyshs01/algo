"""
Solved
20220414
17404.py
RGB거리 2
"""

import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]
# if n ==2:
#     print(min([li[0][i]+li[1][j] for i in range(3) for j in range(3) if i!=j]))
#     exit()
# if n==3:
#     print(min([li[0][i] + li[1][j] + li[2][3-i-j] for i in range(3)for j in range(3) if i!=j]))
INF = 98765431

#dp[i] : 3x3
#i번째로 고른 색 (R,G,B) * 처음 고른 색(R,G,B)

ans = INF
for first in range(3):
    dp = [[INF]*3 for _ in range(n)]
    dp[0][first] = li[0][first]
    for i in range(1,n-1):
        dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + li[i][0]
        dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + li[i][1]
        dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + li[i][2]
    last1 = (first+1)%3
    last2 = 3-first-last1
    dp[n-1][last1] = min(dp[n-2][first],dp[n-2][last2]) + li[n-1][last1]
    dp[n-1][last2] = min(dp[n-2][first],dp[n-2][last1]) + li[n-1][last2]
    now = min(dp[n-1])
    if now < ans:ans = now

print(ans)
    
