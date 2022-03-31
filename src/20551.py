import sys
input = sys.stdin.readline
import bisect
n, m = map(int,input().split())

arr = []
for __ in range(n):
    arr.append(int(input()))
arr.sort()
for __ in range(m):
    num  = int(input())
    pos = bisect.bisect_left(arr,num)
    if pos < n and arr[pos] == num:
        print(pos)
    else:
        print(-1)