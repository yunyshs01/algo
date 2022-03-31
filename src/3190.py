import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
k = int(input())

apples = []
mp = {(i,j):0 for i in range(n) for j in range(n)}


for i in range(k):
    x,y = map(int,input().split())
    mp[(x-1,y-1)] = 2

l = int(input())

turn = {}

for i in range(l):
    x,y = input().split()
    turn[int(x)] = y


t = 0
mp[(0,0)] = 1

dcd = [(0,1),(1,0),(0,-1),(-1,0)]
nowd = 0
q = deque([])
q.append((0,0))
while True:
    t+=1
    nxt = q[-1][0] + dcd[nowd][0],q[-1][1] + dcd[nowd][1]
    if nxt[0] >=n or nxt[0]<0 or nxt[1] >=n or nxt[1]<0 or mp[nxt] == 1:
        print(t)
        break
    apple =  mp[nxt]  == 2

    mp[nxt]=1
    q.append(nxt)
    if not apple:
        mp[q[0]] = 0
        q.popleft()
    
    try:
        if turn[t] == 'L':
            nowd = (nowd+3)%4
        else:
            nowd = (nowd+1)%4
    except:
        pass



    