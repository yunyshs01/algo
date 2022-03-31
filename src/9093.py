import sys
input = sys.stdin.readline

t = int(input())

for ____ in range(t):
    li = input().split()
    li = list(map(lambda x: x[::-1],li))
    print(*li)
