"""
Solved
20220413
2143.py
두 배열의 합
"""


import sys
from bisect import *
input = sys.stdin.readline

t = int(input())
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

ssA = []
ssB = []
#A와 B의 모든 [i,j]의 부분합들을 리스트에 추가한 뒤, 
#A의 부분합을 순회하며, B의 부분합과의 합이 t가 되는 값을 B의 부분합에서 찾는다.
#B의 부분합에서 원하는 값을 찾기 위해 B의 부분합을 정렬해주고,
#lowerbound 와 upperbound 의 차이(=해당 배열에서 찾는 값의 개수)를 구해 정답을 찾는다.

for i in range(n):
    cum = A[i]
    ssA.append(cum)
    for j in range(i+1,n):
        cum+=A[j]
        ssA.append(cum)

for i in range(m):
    cum = B[i]
    ssB.append(cum)
    for j in range(i+1,m):
        cum+=B[j]
        ssB.append(cum)

ans = 0

ssB.sort()
for i in range(len(ssA)):
    lo = bisect_left(ssB,t-ssA[i])
    hi = bisect_right(ssB,t-ssA[i])
    ans+=hi-lo
print(ans)

