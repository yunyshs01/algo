import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())

li = list(map(int,input().split()))
INF = 1000000001
lis = [-INF]
idc = [-1]
parent = {}
for i in range(n):
    idx = bisect_left(lis,li[i])
    if idx == len(lis):
        parent[i] = idc[-1]
        lis.append(li[i])
        idc.append(i)
    else:
        parent[i] = idc[idx-1]
        lis[idx] = li[i]
        idc[idx] = i

print(len(lis)-1)
ans = []
idx = idc[-1]
while True:
    try:
        ans.append(li[idx])
        idx = parent[idx]
    except KeyError:
        ans.pop()
        break

print(' '.join(map(str,ans[::-1])))


        


