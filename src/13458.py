import sys
input = sys.stdin.readline
import math

n = int(input())

a = list(map(int,input().split()))
b,c = map(int,input().split())


def solution(x):
    global b, c
    if x<=b:return 1
    return math.ceil((x-b)/c) + 1

print(sum(map(solution, a)))