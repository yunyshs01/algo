import sys
input = sys.stdin.readline


alphas = 'abcdefghijklmnopqrstuvwxyz'
dic = {a:(num) for num,a in enumerate(alphas)}

txt = input().strip()
key = input().strip()
l = len(key)
for i, c in enumerate(txt):
    if c == ' ':
        print(' ',end='')
        continue
    pos = dic[c] - dic[key[i%l]] - 1
    while pos<0:
        pos+=26
    print(alphas[pos],end='')
