import sys
input = sys.stdin.readline

from itertools import permutations



n = int(input())
dc = {}
li = []
for _ in range(n):
    txt = (list(input().strip()))
    li.append(txt)
    for j in txt:
        dc[j] = -1


def stoi(st):
    n = list(map(lambda x : dc[x],st))
    if len(n)>1 and n[0] == 0:n = n[1:]
    return int(''.join(map(str,n)))

keys = dc.keys()
mx = -1
for perm in permutations(range(10 - len(dc),10),len(dc)):
    for key,val in zip(keys,perm):
        dc[key] = val
    
    ret = sum(map(lambda st: stoi(st), li))
    if ret > mx:mx = ret

print(mx)
    


