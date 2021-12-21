'''


코딩테스트 연습
블록 이동하기

'''

from collections import deque


# 구현 부분
def get_next_pos(pos, MAP):
    next_pos = []  # 반환 결과(이동 가능한 위치들)
    pos = list(pos)  # 현재 위치 정보를 리스트로 변환(집합 -> 리스트)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    # 상 하 좌 우 로 이동하는 경우에 대해서 처리

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        next_pos1_x, next_pos1_y, next_pos2_x, next_pos2_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + \
                                                             dy[i]
        if MAP[next_pos1_x][next_pos1_y] == 0 and MAP[next_pos2_x][next_pos2_y] == 0:
            next_pos.append({(next_pos1_x, next_pos1_y), (next_pos2_x, next_pos2_y)})

    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:

        for i in [-1, 1]:  # 위쪽으로 회전하거나, 아래쪽으로 회전

            # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면 => 회전이 가능한 부분만 확인한다!
            # 두개가 같이 이동해야 하니깐 and 키워드르 쓰는 것
            if MAP[pos1_x + i][pos1_y] == 0 and MAP[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 현재 로봇이 세로로 놓여 있는 경우
    elif pos1_y == pos2_y:
        for i in [-1, 1]:  # 왼쪽으로 회전하거나, 오른쪽으로 회전 하는 경우
            if MAP[pos1_x][pos1_y + i] == 0 and MAP[pos2_x][pos2_y + i] == 0:
                # 왼쪽 오른쪽 두 칸이 모두 비어 있다면,
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos


def solution(board):
    # bfs 순서
    # 1.맵 구성
    n = len(board)
    new_MAP = [[1] * (n + 2) for _ in range(n + 2)]

    for i in range(n):
        for j in range(n):
            new_MAP[i + 1][j + 1] = board[i][j]

    # 맵의 외곽에 벽을 두는 형태로 맵 변형

    # 2. 큐 생성, 초기값 설정

    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)

    # 큐가 빌떄까지 반복
    while q:
        pos, cost = q.popleft()
        # (n, n)위치에 로봇이 도착했다면, 최단 거리 이므로 반환
        if (n, n) in pos:
            return cost

        # 현재 위치에서 이동할 수 있는 위치 확인

        for next_pos in get_next_pos(pos, new_MAP):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리

            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)

    return 0


