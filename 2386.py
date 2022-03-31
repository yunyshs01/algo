import sys
input = sys.stdin.readline

while True:
    li = input().split()
    c = li[0]
    if len(li) == 1 and c == '#':
        break
    st = ' '.join(li[1:])
    cnt = 0
    for char in st:
        if char == c or char == c.upper():
            cnt+=1
    print(c,cnt)

    