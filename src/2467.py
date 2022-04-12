"""
Solved
20200411
2467.py
용액
"""



import sys
input = sys.stdin.readline

n = int(input())
li=list(map(int,input().split()))


l = 0
r = n-1

ret = li[l],li[r]
mn = abs(li[l]+li[r])
while r>l:
    cur =li[r]+li[l]
    if abs(cur) < mn:
        mn = abs(cur)
        ret = li[l],li[r]
    
    if cur<0:
        l+=1
    else:
        r-=1

print(*ret)





