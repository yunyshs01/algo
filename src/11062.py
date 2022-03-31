import sys
input = sys.stdin.readline


t = int(input())

def dfs(beg,end):
    global li,dp,S
    if dp[beg][end]:return dp[beg][end]
    if end == beg:
        ret = li[beg]
        dp[beg][end] = ret
        return ret
    # sum (beg<=i<=end )  ==> S[end] - S[beg-1]
    first = (S[end] - S[beg]) - dfs(beg+1,end) + li[beg]
    last = (S[end-1] - S[beg-1]) - dfs(beg,end-1) + li[end]
    dp[beg][end] = max(first,last)
    return dp[beg][end]


for ____ in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    S = [li[0]]
    for i in range(1,n):
        S.append(S[-1] + li[i])
    S.append(0)
    dp = [[0]*n for _ in range(n)]
    ans = dfs(0,n-1)
    print(ans)


