'''


인구이동


bfs로 풀면 좋을거 같다..!

dfs 풀이도 풀어보기!

'''



from collections import deque

#땅의크기(N) 



N, L, R = map(int, input().split())


#전체 나라의 정보(N x N)를 입력받기

MAP = [list(map(int, input().split())) for _ in range(N)]

#벡터 배열 -> for bfs의 이동

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

#특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신


def bfs(row, col, index):

    #(x, y)의 위치와 연결되 나라(연합) 정보를 담는 리스트
    united = []
    united.append((row, col))
    
    #큐 생성
    q = deque()
    #초기 값 생성
    q.append((row, col))
    union[row][col] = index #현재 연합의 번호 할당
    summary = MAP[row][col] #현재 연합의 전체 인구수 
    count = 1 #현재 연합의 국가 수
    
    #큐가 빌떄까지 반복
    while q:
        row, col  = q.popleft()
        # 현재 위치에서 4가지 방향 모두 다 확인
        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]
            
            #바로 옆에 있는 나라를 확인하며
            #해당 되는 부분 안으로 넣기
            #범위 안에 있고, 안가 본곳(visited 배열 사용)
            if 0 <= next_row < N and 0 <= next_col < N and union[next_row][next_col] == -1:
                #옆에 있는 나라의 인구 차이가 L명이상 R명 이하라면
                if L <= abs(MAP[next_row][next_col] - MAP[row][col]) <= R:
                    #값 넣고, 기록하고, 연합에도 추가!
                    q.append((next_row, next_col))
                    union[next_row][next_col] = index
                    summary += MAP[next_row][next_col]
                    count += 1
                    united.append((next_row, next_col))
                    
    #연합 국가끼리 인구를 분배
    for row, col in united:
        MAP[row][col] = summary // count
    return count
                    

#더 이상 인구 이동을 할 수 없을떄까지 반복
total_count = 0
while True:
    union = [[-1] * N for _ in range(N)] #visited배열의 역활을 함
    index = 0
    for row in range(N):
        for col in range(N):
            if union[row][col] == -1: #해당 나라가 아직 처리되지 않았다며
                bfs(row, col, index)
                index += 1 #union 배열의 값이 됨 / 각각 연합의 번호

    if index == N * N:
        break
    total_count += 1


print(total_count)