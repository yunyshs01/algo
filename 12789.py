import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int,input().split()))

st = []

next = 1
while next <=n:
    if len(li)>0 and li[0] == next:
        li.pop(0)
        next+=1
    elif len(st)>0 and st[-1] == next:
        st.pop(-1)
        next+=1
    elif len(li)>0:
        st.append(li.pop(0))
    else:
        print("Sad")
        break

        
else:
    print("Nice")


    