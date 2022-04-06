"""
Solved
20220406
10422.py
괄호
"""


import sys
input = sys.stdin.readline
M = 1000000007
li = [0]*5001

li[2]=1
li[0] = 1
for i in range(4,5001,2):
    for j in range(2,i+1,2):
        li[i] = (li[i] +  (li[i-j] * li[j-2])%M)%M


t = int(input())
for __ in range(t):
    n = int(input())
    print(li[n])
        



