a,r,n,m = map(int,input().split())

def power(x,n):
    global m
    if n == 0 or x == 1 : return 1
    if n%2 == 1: return (x%m * power(x,n-1))%m
    return (power(x,n//2)**2)%m



def arn(a,r,n):
    global m
    a = a%m
    if n == 0 : return 1
    half = arn(a,r,n//2)
    if n%2 == 0:
        return (half + power(a,n//2) * half)%m
    else:
        return (a + (a * half)%m + power(a,n//2)*half)%m
    

print(arn(a,r,n))
