
"""
Solving
20200412
12015.py
가장 긴 증가하는 부분 수열 2
"""


import sys
from bisect import *
input = sys.stdin.readline

n = int(input())
li = list(map(int,input().split()))

dp = [li[0]]


for i in range(1,n):
    idx = bisect_left(dp,li[i])
    if idx == len(dp):
        dp.append(li[i])
    else:
        dp[idx] = li[i]

print(len(dp))

