import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
t = int(input())
E = [] # Edge
P = [] # Parent
belong = [] # scc그룹에 들어와있는지
S = [] # 스택
vid = 0
inDeg = []
scc = []
SCCmap = {}


def dfs(x):
    global vid
    global SCCcnt
    vid+=1
    P[x] = vid

    parent = P[x]
    S.append(x)

    for i in E[x]:
        if P[i] == 0:
            parent = min(parent,dfs(i))
        if belong[i] == 0:
            parent = min(parent,P[i])
    
    if parent == P[x]:
        SCCmap[P[x]] = len(scc)
        scc.append([])
        while 1:
            top = S.pop()
            scc[-1].append(top)
            belong[top] = P[x]
            if top == x:break
    
    return parent


for ____ in range(t):
    n, m = map(int,input().split())
    E = [[] for i in range(n+1)]
    P = [0] * (n+1)
    belong = [0] * (n+1)
    S = []
    scc = []
    inDeg = [0] * (n+1)
    vid = 0
    SCCcnt = 0
    SCCmap = {}
    for __ in range(m):
        a,b = map(int,input().split())
        E[a].append(b)
    for i in range(1,n+1):
        if not belong[i]:
            dfs(i)
    inDeg = [0] * len(scc)
    for i in range(1,n+1):
        for j in E[i]:
            if belong[i]!=belong[j]:
                inDeg[SCCmap[belong[j]]]+=1
    print(inDeg.count(0))

