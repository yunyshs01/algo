"""
Solving
20200404
1525.py
퍼즐
"""

import sys
from collections import defaultdict
input = sys.stdin.readline
li = []
for _ in range(3):
    li.extend(list(map(int,input().split())))

visit = defaultdict(bool)
visit[tuple(li)] = True
q = [(tuple(li),0)]




ans = -1
while q:
    seq , t = q.pop(0)
    zidx = seq.index(0)
    if seq == (1,2,3,4,5,6,7,8,0):
        ans = t
        break
    
    for dy, dx in zip((-1,0,1,0),(0,1,0,-1)):
        ny,nx = divmod(zidx,3)
        ny+=dy
        nx+=dx
        if ny>=3 or ny<0 or nx>=3 or nx<0:continue
        nidx = ny*3+nx
        nseq = list(seq)
        nseq[zidx] = nseq[nidx]
        nseq[nidx] = 0
        nseq = tuple(nseq)
        if not visit[nseq]:
            visit[nseq] = True
            q.append((nseq, t+1))

print(ans)
        




