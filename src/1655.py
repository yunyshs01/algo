import sys
input = sys.stdin.readline

import heapq as hq


L = []
H = []

n = int(input())
for i in range(n):
    x = int(input())

    if len(L) == 0 or len(H) == 0 or x <= H[0]:
        hq.heappush(L,-x)
    else:
        hq.heappush(H,x)
    
    if len(L) > len(H) + 1:
        hq.heappush(H,-hq.heappop(L))
    
    if len(H) > len(L):
        hq.heappush(L,-hq.heappop(H))
    print(-L[0])
    
    