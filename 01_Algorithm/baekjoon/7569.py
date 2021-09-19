'''


토마토

교수님하고 푼것 복습하고 다시 오자!



3차원이네! 높이까지 계산 해보자! dr , dc, dh(height)까지!

3차원 배열?! 어색한데?!


'''


# rd3_list = [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
#             [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]],
#             [[25, 26, 27, 28], [29, 30, 31, 32], [33, 34, 35, 36]]]
#
#
# print(rd3_list[0])



from collections import deque
import sys


#
# M 상자의 가로 칸의 수 => COL
# N 상자의 세로 칸의 수 => ROW
# H 상자의 높이
#1 그래프 구성
M, N, H = map(int, sys.stdin.readline().split())
MAP = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]




#2 queue 생성
q = deque()


#3 시작점 세팅
for hei in range(H):
    for row in range(N):
        for col in range(M):
            if MAP[hei][row][col] == 1:
                q.append([hei, row, col])

ans = -1

#7. 4 ~ 6 단계 반복

while q :

    #4. 시작점 큐에서 뽑기!
    now = q.popleft()
    now_hei = now[0]
    now_row = now[1]
    now_col = now[2]
    ans = MAP[now_hei][now_row][now_col] #MAP자체를 비지트 배열로 사용!

    #5. next를 찾기! => 델타 배열 사용!
    #이거 헷갈린다,,
    #위, 아래, 왼쪽, 오른쪽, 앞, 뒤
    dr = [0, 0, 0, 0, 1, -1]
    dc = [0, 0, -1, 1, 0, 0]
    dh = [-1, 1, 0, 0, 0, 0]

    for i in range(6):

        next_row = now_row + dr[i]
        next_col = now_col + dc[i]
        next_hei = now_hei + dh[i]

        #범위 벗어나는 것!
        if next_row < 0 or next_col < 0 or next_hei < 0 or next_row >= N or next_col >= M or next_hei >= H:
            continue
        # 이미 익은 토마도는 무시!
        if  MAP[next_hei][next_row][next_col] !=0 :
            continue

        #6. next를 큐에 넣기!
        MAP[next_hei][next_row][next_col] = MAP[now_hei][now_row][now_col] + 1
        q.append([next_hei, next_row, next_col])


#모든 토마토가 익어 가는데 필요한 시간 적기!

for hei in range(H):
    for row in range(N):
        for col in range(M):
            if MAP[hei][row][col] == 0:
                ans = 0
#bfs를 다 돌고도 0인 점이 있으면 모두 익지 못하는 상황
#이미 다 익은 토마토가 있다면 델타배열돌지 않고, 맵을 넣는 상황에서 ans에 1이 들어가고 여기서 0으로 계산
#그게 아니라면 -1로 일수 구하기!
print(ans - 1)



