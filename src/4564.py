import sys
input = sys.stdin.readline

while True:
    a = int(input())
    if a == 0 : break
    st = str(a)
    
    print(st, end = ' ')
    while len(st)>1:
        num = 1
        for c in st:
            num*= int(c)
        st = str(num)
        print(st, end = ' ')
    print()
    
