import sys
input = sys.stdin.readline

n = int(input())
li = map(int,input().split())

dc = {}
for num in li:
    try:
        dc[num]+=1
    except KeyError:
        dc[num] = 1

m = int(input())

li = map(int,input().split())

for num in li:
    try:
        print(dc[num],end = ' ')
    except KeyError:
        print(0, end = ' ')