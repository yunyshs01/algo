"""
Solved
20200406
16637.py
괄호 추가하기
"""

import sys
input = sys.stdin.readline

n = int(input())
fm = input()

nums = list(map(int,fm[::2]))
ops = fm[1::2]

nn = len(nums)

par = [False]* (nn)


def calc(n1, op1, n2):
    if op1 == '+':
        return n1+n2
    if op1 == '-':
        return n1-n2
    if op1 == '*':
        return n1*n2
    

def dfs(x):
    if x == nn:
        li = []
        cop = []
        for i in range(nn):
            if  i>0 and par[i-1]:continue
            if par[i]:
                li.append(calc(nums[i],ops[i],nums[i+1]))
                cop.append(ops[i+1])
            else:
                li.append(nums[i])
                cop.append(ops[i])
            
        ans = li[0]
        for i in range(len(cop)-1):
            ans=calc(ans,cop[i],li[i+1])
        return ans      
                

    ans = -1<<31 -1

    if x>0 and par[x-1]or x == nn-1:
        return dfs(x+1)
    
    ret = dfs(x+1)
    if ret>ans:ans = ret
    par[x] = True
    ret = dfs(x+1)
    if ret>ans:ans = ret
    par[x] = False
    return ans


print(dfs(0))