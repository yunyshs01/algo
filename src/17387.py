
L1 = list(map(int,input().split()))
L2 = list(map(int,input().split()))

def ccw(p1,p2,p3):
    return p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p1[1]*p2[0] - p2[1]*p3[0] - p3[1]*p1[0]


p1 = L1[:2]
p2 = L1[2:]
p3 = L2[:2]
p4 = L2[2:]

first = ccw(p1,p2,p3)
second = ccw(p1,p2,p4)

def swap(x,y):
    t = x
    x = y
    y = t

if first == 0 and second == 0:
    if p1[0] == p2[0]:
        p1 = p1[::-1]
        p2 = p2[::-1]
        p3 = p3[::-1]
        p4 = p4[::-1]
    if(p1>p2):swap(p1,p2)
    if(p3>p4):swap(p3,p4)
    if p3>=p2:
        print(1)
    elif 



elif first * second<=0:
    third = ccw(p3,p4,p1)
    fourth = ccw(p3,p4,p2)
    if third*fourth<=0:
        print(1)
    else:
        print(0)
else:
    print(0)