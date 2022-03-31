import sys
m, n = map(int,sys.stdin.readline().split())

li = [1] * 1000001
li[1] = 0
for i in range(1000001):
    if i<2: continue
    if li[i]:
        if i>=m and i<=n:
            print(i)
        li[i::i] = [0] * len(li[i::i])
        li[i] = 1