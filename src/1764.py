import sys

input = sys.stdin.readline

n, m = map(int,input().split())

s1 = set()
s2 = set()

for i in range(n):
    name = input().strip()
    s1.add(name)
for i in range(m):
    name = input().strip()
    s2.add(name)
li = list(s1&s2)

print(len(li))
li.sort()
for i in li:
    print(i)
