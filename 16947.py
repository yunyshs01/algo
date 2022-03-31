import sys
input = sys.stdin.readline

n = int(input())
li = [[] for _ in range(n)]
visit = [False]*n
for _ in range(n):
    a, b =  map(int,input().split())
    li[a-1].append(b-1)
    li[b-1].append(b-1)





st = [(0,-1)]
visit[0] = True
while st:
    now, pre = st[-1]
    v = li[now]

    pushed = False
    for x in v:
        



    

    