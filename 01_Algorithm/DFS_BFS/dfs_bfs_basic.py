from collections import deque



def bfs(sraph, start, visted):

  #큐(queue) 구현을 위해 deque라이브러리르 사용
  queue = deque([start])
  #현재 노드를 방문 처리
  visted[start] = True
  #큐가 빌 때가지 반복
  while True:
    #큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end=" ")
    #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]:
      if not visted[i]:
        queue.append(i)
        visted[i] = True


#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
[],
[2,3,8],
[1,7],
[1,4,5],
[3,5],
[3,4],
[7],
[2,6,8],
[1,7]

]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visted = [False] * 9



bfs(graph, 1, visted)


INF = 99999999999999 #무한의 비용 선언

#이차원 리스트를 이용해 인접 행렬 표현

graph = [
  [0, 7, 5],
  [7, 0, INF],
  [5, INF, 0]
]




graph = [[] for _ in range(3)]

graph[0].append((1,7))
graph[0].append((2,5))


graph[1].append((0,7))

graph[2].append((0,5))


print(graph)

def dfs(graph, v, visetd):
  #현재 노드를 방문 처리
  visetd[v] = True
  print(v, end= ' ')
  #현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visetd[i]:
        dfs(graph, i, visetd)


graph = [
[],
[2,3,8],
[1,7],
[1,4,5],
[3,5],
[3,4],
[7],
[2,6,8],
[1,7]

]

visted = [False] * 9



dfs(graph, 1, visted)

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()


def recursive_function(i) : 


  if i == 100:
    return


  print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다')
  recursive_function(i + 1)
  print(i, "번째 재귀 함수를 종료합니다.")


recursive_function(1)



def factorial_iterative(n):
    result = 1


    for i in range(1, n + 1):
      result *= i 
    return result

def factorial_recursive(n):
    if n <= 1:
      return 1
    return n * factorial_recursive(n-1)

print(factorial_iterative(5))
print(factorial_recursive(5))








stack = []

stack.append(5) 
stack.append(2)
stack.append(3)
stack.append(7)
stack.append(5)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop


print(stack)
print(stack[::-1])





#N, M을 공백으로 구분하여 입력받기


n, m = map(int, input().split())


#2차원 리스트의 맵 정보 입력받기 
graph = []

for i in range(n):
  graph.append(list(map(int, input())))



#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문


def dfs(x, y):
  #주어진 범위를 벗어나는 경우에는 즉시 종료
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False

  #현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0:
    #해당 노드를 방문처리
    graph[x][y] = 1
    #상, 하 , 좌, 우의 위치도 모두 재귀적으로 호출
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x +1, y)
    dfs(x, y+1)
    return True
  return False


#모든 노드(위치)에 대하여 음료수 채우기

result = 0
for i in range(n):
  for j in range(m):
    #현재 위치에서 DFS수행
    if dfs(i, j) == True:
      result += 1

print(result)




from collections import deque



#N, M을 공백으로 구분하여 입력받기

n, m = map(int, input().split())

#2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))



#이동할 네 방향 정의(상, 하 , 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


#BFS 소스코드 구현

def bfs(x, y):

  #큐(queue) 구현을 위해 deque라이브러리 사용
  queue = deque()
  queue.append((x,y))

  #큐가 빌 때가지 반복
  while queue:
    x, y = queue.popleft()
    #현재 위치에서 네 방향으로의 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      #미로 찾기 공간을 벗어난 경우 무시
      if nx < 0 or ny < 0 or nx >= n or ny >= m :
        continue

      # 괴물이 있으면 못가니깐!
      if graph[nx][ny] == 0:
        continue

      #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

  # 가장 오른쪽 아래까지의 최단 거리 반환
  return graph[n-1][m-1]



#bfs를 수행한 결과 출력
print(bfs(0,0))