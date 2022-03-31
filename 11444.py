#           
#  ( [[1,1], )^n = ([[Fn+1, Fn],)
#    [1,0]]          [Fn,  Fn-1]
#

MOD = 1000000007

F = {}

def matmul(A,B):
    return ((A[0]*B[0])%MOD + (A[1]*B[1])%MOD)%MOD, ((A[0]*B[1])%MOD + (A[1]*B[2])%MOD)%MOD, ((A[1]*B[1])%MOD + (A[2]*B[2])%MOD)%MOD

def fib(n):
    try:
        return F[n]
    except KeyError:pass
    if n == 0:
        F[0] = 0,0,0
        return F[0]
    if n == 1: 
        F[1] = 1,1,0
        return F[1]
    
    if n%2 == 1:
        F[n] = matmul(fib(n-1),F[1])
        return F[n]
    
    half = fib(n//2)
    F[n] =  matmul(half,half)
    return F[n]

n = int(input())

print( fib(n)[1])


