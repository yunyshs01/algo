import sys
input = sys.stdin.readline

n = int(input())

sets = [i for i in range(n)]
ns = {i:1 for i in range(n)}
li = []
def getRoot(x):
    if sets[x] == x:return x
    return getRoot(sets[x])

def union(a,b):
    a = getRoot(a)
    b = getRoot(b)
    if a == b:return
    if a > b:a,b = b,a
    sets[b] = sets[a]
    ns[a]+=ns[b]
    del ns[b]

def outer(p1,p2,p3):
    v1 = p2[0]-p1[0],p2[1]-p1[1]
    v2 = p3[0]-p2[0],p3[1]-p2[1]

    return v1[0]*v2[1] - v1[1]*v2[0]

def chk(s1,s2):
    if s1[0]>s1[1]: s1 = s1[1],s1[0]
    if s2[0]>s2[1]: s2 = s2[1],s2[0]

    o1 = outer(s1[0],s1[1],s2[0])
    o2 = outer(s1[0],s1[1],s2[1])
    o3 = outer(s2[0],s2[1],s1[0])
    o4 = outer(s2[0],s2[1],s1[1])
    if o1==0 and o2 == 0:
        if s1[0] == s2[0]:
            return True
        if s1[0] < s2[0]:
            if s1[1] < s2[0]:
                return False
            return True
        
        if s2[1] < s1[0]:
            return False
        return True

    elif o1 * o2 <=0:
        if o3*o4 <=0:
            return True
        return False
    else:
        return False



for __ in range(n):
    seg = tuple(map(int,input().split()))
    seg = (seg[0],seg[1]),(seg[2],seg[3])
    li.append(seg)

for i in range(1,n):
    for j in range(i):
        flag = chk(li[i],li[j])
        if flag:
            union(i,j)

print(len(ns))
print(max(ns.values()))



