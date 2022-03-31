import sys

n  = int(sys.stdin.readline())

li = [0]*(n+1)
#1 : 선공 승리
#0 : 후공 승리
li[1] = 0
li[2] = 1
li[3] = 0

#i번째 턴에는 i-1번째 혹은 i-3번째에 후공승리가 존재한다면 선공이 승리한다.

for i in range(4,n+1):
    li[i] = int( li[i-1] == 0 or li[i-3] == 0)

print('SK' if li[n] else 'CY')

#print(li)