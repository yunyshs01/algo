"""
Solved

20220331
1062.py
가르침

"""

import sys
input = sys.stdin.readline
n, k = map(int,input().split())
from itertools import combinations

li = [input().strip() for _ in range(n)]
table = [0]*n

for i in range(n):
    for c in li[i]:
        table[i] |= (1<<(ord(c) - ord('a')))

mx = -1
for nums in combinations(range(26),k):
    known = 0
    cnt = 0
    for num in nums:
        known |= 1<<num
    
    for num in table:
        if known & num == num:
            cnt+=1
    if cnt > mx:mx = cnt

print(mx)
    
