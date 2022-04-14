"""
Solved
20220412
13976.py
타일 채우기 2
"""


MOD = 1000000007



N = int(input())
if N%2:
    print(0)
    exit()


def mpow(X, n):
    if n == 0:return 1,0,0,1
    if n == 1:return tuple(map(lambda x: (x+MOD)%MOD,X))
    if n%2 == 1:
        tmp = mpow(X,n-1)
        ret = [0,0,0,0]
        ret[0] = ((X[0]*tmp[0]+MOD)%MOD + (X[1]*tmp[2]+MOD)%MOD)%MOD
        ret[1] = ((X[0]*tmp[1]+MOD)%MOD + (X[1]*tmp[3]+MOD)%MOD)%MOD
        ret[2] = ((X[2]*tmp[0]+MOD)%MOD + (X[3]*tmp[2]+MOD)%MOD)%MOD
        ret[3] = ((X[2]*tmp[1]+MOD)%MOD + (X[3]*tmp[3]+MOD)%MOD)%MOD
        return tuple(ret)
    half = mpow(X,n//2)
    ret = [0,0,0,0]
    ret[0] = ((half[0]*half[0]+MOD)%MOD + (half[1]*half[2]+MOD)%MOD)%MOD
    ret[1] = ((half[0]*half[1]+MOD)%MOD + (half[1]*half[3]+MOD)%MOD)%MOD
    ret[2] = ((half[2]*half[0]+MOD)%MOD + (half[3]*half[2]+MOD)%MOD)%MOD
    ret[3] = ((half[2]*half[1]+MOD)%MOD + (half[3]*half[3]+MOD)%MOD)%MOD
    return tuple(ret)



tmp = mpow((4,-1,1,0),N//2)
print((tmp[0] + tmp[1]+MOD)%MOD)

