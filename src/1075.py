n = int(input())
f = int(input())

mod = n%f

left = n%100

ans = (left - mod)

if ans < 100:
    ans+=100


print(f'{ans:02d}')