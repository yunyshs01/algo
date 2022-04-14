"""
Solved
20220412
17387.py
선분 교차 2
"""


A = list(map(int,input().split()))
B = list(map(int,input().split()))

A = [(A[0],A[1]),(A[2],A[3])]
A.sort()
B = [(B[0],B[1]),(B[2],B[3])]
B.sort()
def ccw(p1,p2,p3):
    return p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p1[1]*p2[0] - p2[1]*p3[0] - p3[1]*p1[0]



first = ccw(A[0],A[1],B[0])
second = ccw(A[0],A[1],B[1])

third = ccw(B[0],B[1],A[0])
fourth = ccw(B[0],B[1],A[1])

if first == 0 and second == 0:
    if A[0] == B[0]:
        print(1)
        exit()
    if A[0]<B[0]:
        if A[1] < B[0]:
            print(0)
            exit()
        print(1)
        exit()
    else:
        if B[1] < A[0]:
            print(0)
            exit()
        print(1)
        exit()
elif first * second <=0:

    if third*fourth <=0:
        print(1)
        exit()
    else:
        print(0)
        exit()
else:
    print(0)
    exit()
