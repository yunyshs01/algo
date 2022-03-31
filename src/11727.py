n = int(input())

ans = [0]*1001

ans[1] = 1
ans[2] = 3

for i in range(3,n+1):
    ans[i] = (ans[i-2]*2 + ans[i-1])%10007


print(ans[n])