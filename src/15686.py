import sys
input = sys.stdin.readline

n, m = map(int,input().split())

mp = [list(map(int,input().split())) for _ in range(n)]

houses = []
rest = {}
for i, li in enumerate(mp):

    while True:
        try:
            j = li.index(1)
            houses.append((i,j))
            mp[i][j] = 0
        except ValueError:
            break
    
    while True:
        try:
            j = li.index(2)
            rest[(i,j)] = []
            mp[i][j] = 0
        except ValueError:
            break

for key in rest:
    y,x = key
    for i, j in houses:
        rest[key].append(abs(y-i) + abs(x-j))
    

def solution(num):
    global n, m

    lenh = len(houses)
    li = [101]*lenh
    for i, key in enumerate(rest):
        if (1<<i)&num !=0:
            for idx in range(lenh):
                if rest[key][idx] < li[idx]:
                    li[idx] = rest[key][idx]
    return sum(li)
result = 101*101
for num in range(1,1<<len(rest)):
    cnt = 0
    nnn = num
    while(nnn):
        nnn = nnn&nnn-1
        cnt+=1
    if cnt > m:continue
    ret = solution(num)
    if ret<result : result = ret
print(result)