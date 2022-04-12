"""
Solved
20200412
9527.py
1의 개수 세기
"""


import sys

input = sys.stdin.readline

a,b  = map(int,input().split())
# 0 :0
# 1 :1
# 1 2   :3
# 1 2 2 3   :8
# 1 1 2 2 3 2 3 3 4 :21
# 1 1 2 2 3 2 3 3 4 2 2 3 3 4 3 4 4 5

#4~7 =>(0~3) + 1
#8~15 => (0~7) + 1

#...
#2^n ~ 2^(n+1) - 1 => (0~2^n-1) +2^n

# a_n : 0~2^(n+1)-1 까지의 숫자의 1의 개수

#a_n = S_(n-1) + 2^(n-1)
#S_n = 2 * S_(n-1) + 2^(n-1)
SS = [0]
i = 1

while True:
    if not 10**16 >> i:break
    SS.append(2*SS[-1] + 2**(i-1))
    i+=1

def getAns(x):
    if x == 0 : return 0
    if x == 1:return 1

    lg = 0
    while x>>lg >= 1:
        r = x%(1<<lg)
        lg+=1
    ans = SS[lg-1] + getAns(r) + r + 1
    return ans


print(getAns(b) - getAns(a-1))

        