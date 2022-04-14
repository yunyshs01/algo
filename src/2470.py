"""
Solved
20220412
2470.py
두 용액
"""
import sys
input = sys.stdin.readline
n  = int(input())
li = list(map(int,input().split()))
li.sort()
l,r = 0, n-1

mn = 2000000001
while r>l:
    now = li[l]+li[r]
    if abs(now) < mn:
        mn = abs(now)
        ans = li[l],li[r]
    if now == 0:break
    if now <0:
        l+=1
    else:
        r-=1

print(*ans)

