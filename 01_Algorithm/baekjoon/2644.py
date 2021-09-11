'''


bfs로 풀어보자!


노드의 거리 복습하고 다시 풀어보자!

'''

#기본적인 입력받기
from collections import deque

V = int(input())

#3. 시작점 세팅
start, goal = map(int, input().split())

E = int(input())



#1,  연결구조를 구성, 이차원 리스트 방식
graph = [[] for _ in range(V + 1)] # +1 하는 이유! 0번째 인덱스는 사용하지 않아서! 


for _ in range(E) : #엣지의 수만큼 관계를 정의한다 인덱스번쨰에서 갈 수 있는 곳들!
    FROM, TO  = map(int, input().split())
    graph[FROM].append(TO)
    graph[TO].append(FROM)

#2. 큐 생성

q = deque()
visited = [0] * (V+1) # 한번 간곳을 기억하기 위한 배열 생성


visited[start] = 1
q.append(start)

while len(q) > 0 :
    #4 큐의 맨 앞점을 꺼냄(now)
    now = q.popleft()

    #5 now에서 갈 수 있는 모든 곳 가보자!
    for next in graph[now]:


        if visited[next] != 0:
            continue

        #6 next를 큐에 넣기!

        visited[next] = visited[now] + 1 #촌수 계산을 위해서 몇번째 만에 도착을 했는지 계산
        q.append(next)

if visited[goal] == 0:
        print("-1")
else:
        print(visited[goal] - 1)







