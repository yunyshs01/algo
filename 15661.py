import sys
input = sys.stdin.readline

n = int(input())
ALL1 = 1<<n-1
li = []
for _ in range(n):
    li.append(list(map(int,input().split())))

ans = 40001
dc = {}
for bit in range(1,1<<(n)):
    start = 0
    link = 0
    if dc[bit]:continue
    for i in range(n):
        for j in range(i+1,n):
            team1 =  ((1<<i)&bit)>>i
            team2 = ((1<<j)&bit)>>j
            if team1 ==team2:
                if team1:
                    start+=li[i][j] + li[j][i]
                else:
                    link+=li[i][j]+li[j][i]
    dc[bit] = start
    dc[bit^ALL1] = link
    dif = abs(start-link)
    if dif < ans:
        ans = dif   
print(ans)

            

            