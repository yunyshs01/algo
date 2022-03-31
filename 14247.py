import sys
input = sys.stdin.readline

n = int(input())

now = map(int,input().split())
up = map(int,input().split())

now = list(zip(now,up))

ans = 0

now.sort(key = lambda x:x[1])

for i in range(n):
    ans+= now[i][0] + i * now[i][1]

    

print(ans)
