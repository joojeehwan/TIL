'''


연구소


dfs로도 풀어보고 bfs로도 풀어보자!

조합을 구하는 것 까지 하는 아주 좋은 문제,,!!

'''


# n, m = map(int, input().split())
#
# #초기 맵 리스트
# data = [list(map(int, input().split())) for _ in range(n)]
# #벽을 설치한 뒤의 맵 리스트
# MAP = [[0] * m for _ in range(n)]
#
#
# #바이러스가 갈 수 있는 4가지 방향
# #상 우 하 좌
# dr = [-1, 0, 1, 0]
# dc = [0 , 1, 0, -1]
#
# result = 0
#
# #DFS를 이용해 바이러스 퍼지게 하기
#
# def virus(row, col):
#
#     #바이러스가 갈 수 있는 4방향 모두 다 확인
#     for i in range(4):
#         next_row = row + dr[i]
#         next_col = col + dc[i]
#
#         #바이러스가 퍼질 수 있는 경우 => 맵을 안 벗어남
#         if 0 <= next_row < n and 0 <= next_col < m:
#             #그리고 내가 안가본 벽이 아닌 곳이라면
#             if MAP[next_row][next_col] == 0:
#                 #해당 바이러스를 배치하고, 다시 재귀적으로 수행
#                 MAP[next_row][next_col] = 2
#                 virus(next_row, next_col)
#
#
# def check_safty():
#     safty = 0
#     for row in range(n):
#         for col in range(m):
#             if MAP[row][col] == 0:
#                 safty += 1
#     return safty
#
# #깊이 우선 탐색을 이용해 울타리를 설치하면서, 매번 안전영역의 크기를 계싼
# def dfs(count):
#
#     #변수는 global로 가져가서 풀어제껴버리는,,!!
#     global result
#     #울타리가 3개가 설치된 경우
#     if count == 3:
#         for i in range(n):
#             for j in range(m):
#                 MAP[i][j] = data[i][j]
#
#         #각 바이러스의 위치에서 전파 진행
#         for i in range(n):
#             for j in range(m):
#                 if MAP[i][j] == 2:
#                     virus(i, j)
#
#         result = max(result, check_safty())
#         return
#
#     #빈 공간에 울타리 설치
#     #여기서 조합
#     for i in range(n):
#         for j in range(m):
#             if data[i][j] == 0:
#                 data[i][j] = 1
#                 count += 1
#                 dfs(count)
#                 #설치했다가 다시 뺴야지 다른 조합을 볼 수 있음
#                 # 아 ==이랑 = 하는 오타 좀 이제 그만,,! 제발!!
#                 data[i][j] = 0
#                 count -= 1
#
# dfs(0)
# print(result)


#bfs 풀이
#copy를 써서 풀어도 되는구나!

import sys
import copy
from collections import deque

input = sys.stdin.readline

#상 우 하 좌
dr = [1, 0, -1, 0]
dc = [0, 1, 0,-1]


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
ans = 0
q = deque()

def bfs():
    global ans
    
    #1. 그래프 구성
    after_wall_map = copy.deepcopy(MAP)
    
    #2. 시작점 세팅
    for i in range(N):
        for j in range(M):
            if after_wall_map[i][j] == 2:
                q.append((i, j))

    #while 문 반복 => 큐가 비워질 때 까지!

    while q:
        row, col = q.popleft()
        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]

            if 0<= next_row < N and 0 <= next_col < M :
                if after_wall_map[next_row][next_col] == 0:
                    after_wall_map[next_row][next_col] = 2
                    q.append((next_row, next_col))

    cnt = 0
    for row in after_wall_map:
        #0의 갯수를 전부세서 더해! 한 행씩
        cnt += row.count(0)
    ans = max(ans, cnt)
        
#벽을 세우는 전체의 경우의 수 계산!

def dfs(lev):

    if lev == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 0:
                MAP[i][j] = 1
                dfs(lev + 1)
                MAP[i][j] = 0


dfs(0)
print(ans)


