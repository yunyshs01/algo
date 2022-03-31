
import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    t,x = map(int,input().split())
    if t == 1:
        idx = bisect_left(li,x)
        li.insert(idx,x)
    else:
        print(li[x-1])
        li.pop(x-1)

    