import sys
input = sys.stdin.readline
from heapq import *
T = int(input())

for ____ in range(T):
    k = int(input())
    maxq = []
    minq = []
    s = set()
    for i in range(k):
        st = input().strip()
        op, num = st[0],int(st[2:])
        if op == 'I':
            heappush(maxq, (-num,i))
            heappush(minq, (num,i))
            s.add(i)
        else:
            if num == 1:
                q = maxq
            else:
                q = minq

            while q:
                tgt, id_ = q[0]
                try:
                    s.remove(id_)
                    heappop(q)
                    break
                except KeyError:
                    heappop(q)


            

    if len(s) == 0:
        print('EMPTY')
    else:
        print(-maxq[0][0], minq[0][0])