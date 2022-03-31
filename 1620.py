import sys
input = sys.stdin.readline


n, m = map(int,input().split())

dc = {}
li = ['']

for i in range(n):
    name = input().strip()

    dc[name] = i+1
    li.append(name)

for _ in range(m):
    q = input().strip()

    try:
        num = int(q)
        print(li[num])
    
    except ValueError:
        print(dc[q])
    
