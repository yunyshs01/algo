import sys
input = sys.stdin.readline
M = 1000000007
t = int(input())
li = [[0,0]for _ in range(5001)]

li[0][0] = 1
for i in range(2,5001): 
    if i%2 == 0:
        li[i] = (li[i] + sum(li[i-2])%M)%M
    for j in range(2,i):
        if li[j]>0 and i+j<5001:
            li[i+j] = (li[i + j] + (li[i]*li[j]*2)%M)%M
    if li[i]>0 and 2*i < 5001:
        li[2*i] = (li[2*i] + (li[i]*li[i])%M)%M
for _ in range(t):
    print(li[int(input())])