'''

나이트의 이동


미로의 거리 와 같은 문제이다!! 이걸로 워밍업 해보자!
'''
from collections import deque

T = int(input())

for tc in range(1, T+1):
    I = int(input())

    # 1 연결 구조를 구성
    MAP = [[0] * I for _ in range(I)]

    #2 시작점 세팅
    start_row, start_col = map(int, input().split())
    end_row, end_col = map(int, input().split())


    # 2. 큐 생성
    q = deque()
    visited = [[0] * I for _ in range(I)]

    MAP[end_row][end_col] = 3

    q.append([start_row, start_col])

    result = -1
    while q : #큐에 값이 있고! 도착하기 전!

        now = q.popleft()
        now_row = now[0]
        now_col = now[1]

        dr = [-1, -2, -2, -1, 1, 2, 2, 1]
        dc = [2, 1,-1, -2, -2, -1, 1, 2]
        for i in range(8):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if next_row < 0 or next_col < 0 or next_row >= I or next_col >= I :
                continue

            if visited[next_row][next_col] != 0:
                continue


            visited[next_row][next_col] = visited[now_row][now_col] + 1
            q.append([next_row, next_col])
            if MAP[next_row][next_col] == 3:
                result = visited[next_row][next_col]


    # for row in range(I):
    #     for col in range(I):
    #         if MAP[row][col] == 3 :
    #             result = visited[row][col]

    if result < 0 :
        print(0)
    elif start_row == end_row and start_col == end_col:
       print(0)
    else:
        print(result)



