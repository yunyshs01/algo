import sys
input = sys.stdin.readline

n, m, x, y, k = map(int,input().split())

mp = [list(map(int,input().split()))for i in range(n)]

class dice:
    def __init__(self, num,n,e,s,w,opp):
        self.center = num
        self.n = n
        self.e = e
        self.s = s
        self.w = w
        self.opp = opp
    
    def roll(self,c):
        if c == 1:
            t = self.center
            self.center= self.e
            self.e = self.opp
            self.opp = self.w
            self.w = t
        if c == 2:
            t = self.center
            self.center= self.w
            self.w = self.opp
            self.opp = self.e
            self.e = t
        if c == 3:
            t = self.center
            self.center= self.n
            self.n = self.opp
            self.opp = self.s
            self.s = t
        if c == 4:
            t = self.center
            self.center= self.s
            self.s = self.opp
            self.opp = self.n
            self.n = t
        
mydice = dice(0,0,0,0,0,0)

pos = 0,0

op =list(map(int,input().split()))

dcd = [(0,1),(0,-1),(-1,0),(1,0)]

for i in op:
    ip = i-1
    nxt = (pos[0] + dcd[ip][0],pos[1] + dcd[ip][1])
    if nxt[0]>=n or nxt[0]<0 or nxt[1]>=m or nxt[1]<0:
        continue
    mydice.roll(i)

    if mp[nxt[0]][nxt[1]] == 0:
        mp[nxt[0]][nxt[1]] = mydice.opp
    else:
        mydice.opp = mp[nxt[0]][nxt[1]]
        mp[nxt[0]][nxt[1]] = 0
    print(mydice.center)
        



