import sys
input = sys.stdin.readline
from collections import deque


n, m = map(int,input().split())
E = [[]for _ in range(n+1)]

inDeg = [0] * (n+1)

for _ in range(m):
    a, b = map(int,input().split())
    E[a].append(b)
    inDeg[b]+=1

q = deque()

for i in range(1,n+1):
    if inDeg[i] == 0:
        q.append(i)

ans = []

while len(q):
    top = q.popleft()
    ans.append(str(top))
    for i in E[top]:
        inDeg[i] -=1
        if inDeg[i] == 0:
            q.append(i)

print(' '.join(ans))

