import sys
n = int(sys.stdin.readline())

win = [False] * (n+1)

try:
    win[1] = True
    win[2] = False
    win[3] = True
    win[4] = True


    for i in range(5,n+1):
        win[i] = not win[i-1] or not win[i-3] or not win[i-4]
except IndexError:
    pass
print('SK'if win[n] else 'CY')

