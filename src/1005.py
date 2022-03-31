# 1005.py
# 위상정렬
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int,input().split())
    time =[0] + list(map(int,input().split()))
    E = [[] for i in range(n+1)]
    dp = [-1]*(n+1)
    inDeg = [0] * (n+1)
    for __ in range(k):
        x, y = map(int,input().split())
        E[x].append(y)
        inDeg[y] +=1
    q = deque()
    w = int(input())
    for i in range(1,n+1):
        if inDeg[i] == 0:
            q.append(i)
            dp[i] = time[i]
    while len(q):
        b = q.popleft()
        if b==w:break
        for i in E[b]:
            inDeg[i]-=1
            if inDeg[i] == 0:
                q.append(i)
            if dp[i]<dp[b] + time[i]:
                dp[i] = dp[b] + time[i]
    print(dp[w])
    
