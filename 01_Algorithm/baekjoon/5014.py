'''


스타트 링크


이것도 bfs인거 같은데,, 위아래로만,, 하면 되는거 같은데?!

위아래를 그냥 1차원 배열로 표현해도 되남?!

위로 가는거 아래로 가는건 델타 배열로 표현하면 되나?

'''


import sys
from collections import deque



floor, start, goal, up, down = map(int, sys.stdin.readline().split())

#1 그래프 구성

MAP = [0] * (floor+1) #0층은 사용하지 않으니깐!

#2. queue생성

q = deque()

#3. 시작점 세팅

MAP[0] = -1
MAP[start] = 1
q.append(start)

ans = 0

#7. 4 ~ 6단계 반복

while q:

    #4. 맨 앞점 가져오기!
    now = q.popleft()
    ans = MAP[now]
    if now == goal: #들어온 now가 도착지면 그만 반복 돌고 나가자!
        break

    #5 next를 찾기!
    dc = [up, -down] # 아 down에 "-"넣어야 함! 내려가는 것 표현!
    for i in range(2):
        next_point = now + dc[i]

        if next_point < 1 or next_point > floor: # 범위 벗어나는 것도 가지말자!
            continue

        if MAP[next_point] != 0: #이미 가본곳은 가지말자!
            continue
        #6, next를 큐에 넣기!
        MAP[next_point] = MAP[now] + 1
        q.append(next_point)

if MAP[goal] == 0:
    print("use the stairs")

else:
    print(ans - 1)














