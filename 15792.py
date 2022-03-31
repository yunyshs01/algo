
a,b  = map(int,input().split())


print(a//b, end = '')

if a%b:
    print('.',end = '')
    num = a%b * 10
    print(num//b, end = '')
    cnt = 1
    while(num%b):
        if cnt > 1000:break
        num = num%b * 10
        print(num//b, end = '')
        cnt+=1


