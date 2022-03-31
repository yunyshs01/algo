#20220323
#11659.py

import sys
input = sys.stdin.readline

n, m = map(int,input().split())

li = list(map(int,input().split()))
cum = []
cum.append(0)
for i in range(1,n+1):
    cum.append(cum[-1] + li[i-1])

cum.append(0)

for _ in range(m):
    a,b = map(int,input().split())
    print(cum[b] - cum[a-1])