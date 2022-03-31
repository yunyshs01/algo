"""
Solved
20220330
14002.py
가장 긴 증가하는 부분 수열 4
"""
import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int,input().split()))

lis = [(li[i],)for i in range(n)]


for i in range(1,n):
    for j in range(i-1,-1,-1):
        if li[j] <li[i] and len(lis[j]) >= len(lis[i]):
            lis[i] = *lis[j],li[i]

midx = -1
mlen = 0

for i in range(n):
    if len(lis[i]) > mlen:
        mlen = len(lis[i])
        midx = i

print(mlen)
print(' '.join(map(str,lis[midx])))
