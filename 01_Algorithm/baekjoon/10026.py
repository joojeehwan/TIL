'''


적록색약


이게 왜 bfs이지,,?!

그걸 알아야 한다,, bfs인 이유를 알아야 해!

2차원 배열의 넓이에 대한 문제,,?! bfs/dfs를 생각 해야대!

적록색약용 배열 하나 만들고
일반욕 배열 하나 만들어서
bfs돌고! bfs탐색이 끝날 떄마다(같은 색깔의 칸들을 탐색이 끝날떄마다) cnt를 하나 씩 증가!


'''



from collections import deque


def bfs(start_row, start_col):
    # 상 하 좌 우
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    q.append([start_row, start_col])
    visited[start_row][start_col] = 1

    while q:
        now = q.popleft()
        now_row = now[0]
        now_col = now[1]
        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                continue

            if visited[next_row][next_col] != 0:
                continue

            if MAP[next_row][next_col] == MAP[start_row][start_col]:
                q.append([next_row, next_col])
                visited[next_row][next_col] = 1

                #처음에 들어오는 값들을 검색해야 하니깐! 같은색,,,!

N = int(input())
q = deque()
MAP = [list(map(str, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

#일반 먼저 확인
cnt = 0
for row in range(N):
    for col in range(N):
        if visited[row][col] == 0:
            bfs(row, col)
            cnt += 1
            
print(cnt, end= " ")

#그 다음에 적록색약 확인
for row in range(N):
    for col in range(N):
        if MAP[row][col] == "R":
            MAP[row][col] = "G"

visited = [[0] * N for _ in range(N)]

cnt = 0
for row in range(N):
    for col in range(N):
        if visited[row][col] == 0:
            bfs(row, col)
            cnt += 1
print(cnt)



















