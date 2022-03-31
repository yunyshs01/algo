import sys
input = sys.stdin.readline

t = int(input())

def getRoot(st):
    global mp
    if mp[st] == st:
        return st
    return getRoot(mp[st])

def union(st1,st2):
    global mp, siz
    a = getRoot(st1)
    b = getRoot(st2)
    if a==b:
        return
    if a<=b:
        mp[b] = a
        siz[a]+=siz[b]
    else:
        mp[a] = b
        siz[b]+=siz[a]

for ____ in range(t):
    f = int(input())
    mp = {}
    siz = {}
    for __ in range(f):
        a,b = input().rstrip().split()
        try:
            mp[a]
        except KeyError:
            mp[a] = a
            siz[a] = 1
        try:
            mp[b]
        except KeyError:
            mp[b] = b
            siz[b] = 1
        union(a,b)

        s = getRoot(a)
        print(siz[s])


