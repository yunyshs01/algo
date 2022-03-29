import sys
input = sys.stdin.readline
from collections import defaultdict
n = int(input())

dc = defaultdict(list)

for _ in range(n):
    a, b, c = input().split()
    a = a.upper(); b = b.upper()
    dc[a].append((b,c),[0])