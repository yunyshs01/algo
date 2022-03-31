import sys
from bisect import bisect_left
input = sys.stdin.readline
INF = 1000000001
n = int(input())

li = list(map(int,input().split()))

lis = [-INF]

for i in range(n):
    idx = bisect_left(lis,li[i])
    if idx == len(lis):
        lis.append(li[i])
    else:
        lis[idx] = li[i]

print(len(lis)-1)
