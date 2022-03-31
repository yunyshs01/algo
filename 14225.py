n = int(input())
li = list(map(int,input().split()))

ans = [False]*(20*100000 + 1)
ans[0] = True
dp = [0]*(1<<n)

for i in range(1,1<<n):
    lmb = 0
    while i//(1<<lmb):lmb+=1
    lmb-=1
    dp[i] = dp[i-(1<<lmb)] + li[lmb]
    ans[dp[i]] = True

for i, flag in enumerate(ans):
    if not flag:
        print(i)
        break

