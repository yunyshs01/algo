import sys
from itertools import permutations
input = sys.stdin.readline

k = int(input())
op = input().split()

def chk(li):
    for i, e in enumerate(op):
        if not ((li[i]<li[i+1] if e == '<' else li[i]>li[i+1])):
            return False
    return True
mx = (0,)*(k+1)
mn = (9,)*(k+1)
for li in permutations(range(10),(k+1)):
    if chk(li):
        now = tuple(li)
        if now>mx:mx = now
        if now < mn:mn = now

print(''.join(map(str,mx)))
print(''.join(map(str,mn)))

