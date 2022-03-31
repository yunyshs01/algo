"""
Solved
20220331
10460.py
구슬 탈출 2
"""
import sys

input = sys.stdin.readline
from collections import defaultdict
n, m = map(int,input().split())
table = [input().strip() for _ in range(n)]
# R, B, O : 빨간공, 파란공, 구멍의 y,x 좌표
R = -1,-1
B = -1,-1
O = -1,-1
for i ,st in enumerate(table):
    if R[0] == -1:
        try: R = i, st.index('R')
        except ValueError: pass
    if B[0] == -1:
        try: B = i, st.index('B')
        except ValueError: pass
    if O[0] == -1:
        try: O = i, st.index('O')
        except ValueError: pass

dyx = ((-1,0),(0,1),(1,0),(0,-1))

#ans : 답을 저장할 변수
ans = -1

# BFS 로 순회한다. 처음 R,B 횟수를 큐에 넣고, 4방향으로 기울였을 때의 R, B 의 좌표를 q에 넣는다.
q= [(R,B,0)]

#visit :  R과 B의 좌표를 방문한 적이 있는지를 나타내는 딕셔너리
visit = defaultdict(bool)
visit[(R,B)] = True

#BFS
while q:
    #r,b,t 현재의 빨간공 , 파란공, 기울인 횟수
    r,b,t = q.pop(0)
    if t == 10:
        #이미 기울인 횟수가 10번이라면, 더이상 탐색할 수 없다.
        ans = -1
        break
    # 4방향으로 순회한다.
    for k, (dy,dx) in enumerate(dyx):
        # 구슬을 움직일 때에, 기울이는 방향에 따라 먼저 움직여야하는 구슬을 선택한다.(앞에있는 구슬)
        # r,b의 좌표와 기울이는 방향을 비교하여 먼저 움직이는 구슬을 결정한다.
        if k == 0 or k == 3:
            first,second = ((r,b) if r<b else (b,r))
        else:
            first,second = ((r,b) if r>b else (b,r))
        # fail : 파란 구슬이 들어간 경우 활성화 
        # flag : 빨간 구슬이 들어간 경우 활성화 
        fail  = False
        flag    = False
        for i in range(1,10):
            # nfy, nfx : 먼저 굴릴 구슬의 다음 탐색할 좌표
            nfy = first[0] + dy*i
            nfx = first[1] + dx*i
            # 다음 탐색할 좌표가 벽이라면 마지막 탐색한 좌표로 되돌리고 탐색 중단
            if table[nfy][nfx] == '#':
                nfy -=dy
                nfx -=dx
                break
            # 다음 탐색할 좌표가 구멍이라면, 빨간색이라면 flag 활성화 한후 게임장바깥으로
            # 파란색이라면 fail활성화 한후, 탐색 중단
            if (nfy,nfx) == O:
                if first == r:
                    flag = True
                    nfy,nfx = -1,-1
                else:
                    fail = True
                break
        #먼저 움직인 구슬이 파란색이고, 구멍을 만났다면 바로 실패, 해당방향은 불가능이다.
        if fail:
            continue
        #두번째로 움직이는 구슬
        for i in range(1,10):
            nsy = second[0] + dy*i
            nsx = second[1] + dx*i
            #다음 탐색할 좌표가 벽이거나, 앞서 굴린 좌표라면, 마지막 탐색한 좌표로 되돌리고 탐색 중단
            if table[nsy][nsx] == '#' or (nsy,nsx) == (nfy,nfx):
                nsy -=dy
                nsx -=dx
                break
            # 다음 탐색할 좌표가 구멍이라면 빨간 구슬이면 flag 활성화
            # 파란구슬이면 flag 비활성화, fail 활성화 후, 탐색 종료
            if (nsy,nsx) == O:
                if second == r:
                    flag = True
                else:
                    flag = False
                    fail = True
                break
        # 파란 구슬이 들어갔다면 실패, 이 방향은 불가능
        if fail:
            continue
        # 빨간구슬만 들어갔다면 이 방향은 성공, 탐색 종료
        if flag:
            break

        # 위 두 경우 모두 아니라면, 다음 빨간구슬과 파란구슬의 좌표로 bfs 계속 수행
        #nr : 큐에 넣을 다음 빨간구슬의 좌표,
        #nb : 큐에 넣을 다음 파란구슬의 좌표
        if first == r:
            nr = nfy,nfx
            nb = nsy,nsx
        else:
            nr = nsy,nsx
            nb = nfy,nfx
        # 이미 빨강, 파랑이 그 좌표인 상태였던 적이 있다면 큐에 넣지 않는다.
        if not visit[(nr,nb)]:
            visit[(nr,nb)] = True
            q.append((nr,nb,t+1))
    #방향 탐색이 종료되었을 때에 성공했다면 ans에 답을 적고 bfs 종료
    if flag:
        ans = t+1
        break
#정답 출력
print(ans)





    


