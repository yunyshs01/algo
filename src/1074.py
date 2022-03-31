

def solution(n,r,c):
    if n==1:return r*2 + c

    halflen = 2**(n-1)

    offset = 0

    if (r>=halflen):
        offset += halflen**2 * 2
        r-=halflen
    if (c>=halflen):
        offset += halflen**2
        c-=halflen
    
    return offset + solution(n-1,r,c)

n, r, c = map(int,input().split())

print(solution(n,r,c))
