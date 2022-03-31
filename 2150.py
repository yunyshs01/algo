import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**5)

v, e = map(int,input().split())

E = [[] for i in range(v+1)]


for ___ in range(e):
    a,b = map(int,input().split())
    E[a].append(b)

ans = []
S = []
P = [0] * (v+1)
done = [False] * (v+1)
vid = 0

def dfs(x):
    global vid
    vid+=1
    P[x] =vid 
    S.append(x)

    parent = P[x]
    for i in E[x]:
        # 다음 노드를 방문하지 않았다면 dfs 수행후 낮은 id
        if P[i] == 0: 
            parent = min(parent,dfs(i))
        # 이미 방문한 노드지만, scc에 추가가 안된 노드라면 낮은 id로 바꾸기
        elif not done[i] : parent = min(parent,P[i])
    
    if parent == P[x]:
        scc = []
        while True:
            top = S.pop()
            scc.append(top)
            done[top] = True
            if top == x:break
        ans.append(scc)
    
    return parent

for i in range(1,v+1):
    if P[i] == 0:dfs(i)

print(len(ans))

ans = list(map(sorted,ans))
ans = sorted(ans,key = lambda x: x[0])
for li in ans:
    for i in li:
        print(i,end=" ")
    print(-1)