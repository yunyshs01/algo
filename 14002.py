import sys
<<<<<<< HEAD
input =  sys.stdin.readline
=======

input = sys.stdin.readline
>>>>>>> b792a2baea4a3281e7a2ad822aeeb6c8c7a62ace

n = int(input())
li = list(map(int,input().split()))

<<<<<<< HEAD
dc = [(li[0],)]

for i in range(1,n):

    for j in range(len(dc)):
        if dc[-(j+1)][-1] < li[i]:
            if j==0:
                dc.append((*dc[-(j+1)],li[i]))
            else:
                if li[i] < dc[-j][-1]:
                    dc[-j] = (*dc[-(j+1)],li[i])
            break
        

print(len(dc[-1]))
print(' '.join(map(lambda x : str(x),dc[-1])))
=======
lis = [(li[i],)for i in range(n)]


for i in range(1,n):
    for j in range(i-1,-1,-1):
        if li[j] <li[i] and len(lis[j]) >= len(lis[i]):
            lis[i] = *lis[j],li[i]

midx = -1
mlen = 0

for i in range(n):
    if len(lis[i]) > mlen:
        mlen = len(lis[i])
        midx = i

print(mlen)
print(' '.join(map(str,lis[midx])))
>>>>>>> b792a2baea4a3281e7a2ad822aeeb6c8c7a62ace
