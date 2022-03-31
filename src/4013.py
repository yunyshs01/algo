import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int,input().split())

E = [[] for i in range(n+1)]
M = [0]*(n+1)
P = [0]*(n+1)
belong = [0]*(n+1)
S = []
SCC = []
inDeg = []
SCCmap = {}
sumSCC = []
vid = 0

sccP = []

def dfs(x):
    global vid
    vid+=1
    P[x] = vid
    S.append(x)
    parent = P[x]
    for i in E[x]:
        if P[i] == 0:
            parent = min(parent,dfs(i))
        if belong[i] == 0:
            parent = min(parent,P[i])
    
    if parent == P[x]:
        SCCmap[P[x]] = len(SCC)
        SCC.append([])
        sumSCC.append(0)
        while 1:
            top = S.pop()
            SCC[-1].append(top)
            sumSCC[-1]+=M[top]
            belong[top] = P[x]
            if top == x:break
    return parent


for ___ in range(m):
    a,b = map(int,input().split())
    E[a].append(b)
for i in range(1,n+1):
    a = int(input())
    M[i] = a
s,p = map(int,input().split())
li = list(map(int,input().split()))
for i in range(1,n+1):
    if belong[i] == 0:dfs(i)
sccP = [i for i in range(len(SCC))]

def getP(sccX):
    if sccP[sccX] == sccX:return sccX
    return getP(sccP[sccX])
def unionP(sccA,sccB):
    sccA = getP(sccA)
    sccB = getP(sccB)
    if sccA == sccB : return
    if sccA>sccB : sccP[sccA] = sccB
    else : sccP[sccB] = sccA

for i in range(1,n+1):
    for j in E[i]:
        if belong[i]!=belong[j]:
            unionP(SCCmap[belong[i]],SCCmap[belong[j]])

sSCC = SCCmap[belong[s]]
max = -1
for i in li:
    iSSC = getP(SCCmap[belong[i]])
    ans = 0

    nowP = getP(sSCC)
    iP = getP(iSSC)
    if  nowP == iP:
        for j in range(len(sumSCC)):
            if nowP == getP(j):
                ans+=sumSCC[j]
    if ans > max:
        max = ans
print(max)



