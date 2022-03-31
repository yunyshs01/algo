import sys
input = sys.stdin.readline

n = int(input())
li =  list(map(int,input().split()))

li.sort()

ret = 0
for i in range(n):
    ret+=(n-i)*li[i]

print(ret)
