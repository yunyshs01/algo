import sys
input = sys.stdin.readline


n, m = map(int,input().split())

table = [i for i in range(n+1)]

def getId(x):
    if x == table[x]:return x
    return getId(table[x])

def mergeId(a, b):
    a = getId(a)
    b = getId(b)
    if a>b:table[a] = b
    else : table[b] = a
    

E = [''] * m
cnt = 0
for _ in range(m):
    E[cnt] = tuple(map(int,input().split()))
    cnt+=1

# from operator import itemgetter, attrgetter

#sorted(E,key = itemgetter(2))
E = sorted(E,key=lambda d:d[2])

cost = [0]*(n-1)
cnt = 0
for b, e, w in E:
    if getId(b)!=getId(e):
        cost[cnt] = w
        mergeId(b,e)
        cnt+=1
        if cnt == n-1:break

print(sum(cost)-max(cost))

#append를 사용하는것과 별 시간차이가 없었다~(4ms 더 느림)