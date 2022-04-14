"""
Solved
20220413
12784.py
인하니카 공화국
"""

import sys
input = sys.stdin.readline
def dfs(cur,par):
    ret = 0
    my = 0
    for v, d in E[cur]:
        if v==par:
            my = d
            continue        
        tmp = dfs(v,cur)
        ret+=tmp
    if ret == 0:return my
    return min(ret,my)

t = int(input())
for ___ in range(t):
    n, m= map(int,input().split())

    E = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b,c = map(int,input().split())
        E[a].append((b,c))
        E[b].append((a,c))
    E[1].append((0,98765431))
    ans = dfs(1,0)
    if m == 0:print(0)
    else : print(ans)
