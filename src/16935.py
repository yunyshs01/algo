"""
Solving
20220401
16935.py
배열 돌리기 3
"""

import sys
input = sys.stdin.readline

n, m, r = map(int,input().split())

li = [list(map(int,input().split())) for _ in range(n)]
op = map(int,input().split())
h,w = n,m
for x in op:
    tmp = []
    if x == 1:
        li = li[::-1]
    if x == 2:
        li = list(map(lambda l: l[::-1],li))
    if x == 3:
        li = list(list(map(lambda l:l[i],li))[::-1]for i in range(w))
        h,w = w,h
    if x == 4:
        li = list(list(map(lambda l:l[-i-1],li))for i in range(w))
        h,w = w,h
    if x == 5:
        tmp = []
        for i in range(h//2):
            tmp.append(li[h//2+i][:w//2] + li[i][:w//2])
        for i in range(h//2):
            tmp.append(li[h//2+i][w//2:] + li[i][w//2:])
        li = tmp

        
    if x == 6:
        tmp = []
        for i in range(h//2):
            tmp.append(li[i][w//2:] + li[h//2+i][w//2:])
        for i in range(h//2):
            tmp.append(li[i][:w//2] + li[h//2+i][:w//2])
        li = tmp

print('\n'.join(map(lambda l: ' '.join(map( str,l)),li)))