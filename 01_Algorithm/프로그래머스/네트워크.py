#dfs / bfs 풀이

def dfs(root, visited, computers):
    visited[root] = True #방문여부 표시
    for i in range(len(visited)): #N = len(visted)
     #root - i 가 연결되어 있고, 방문하지 않은 곳이라면
        if computers[root][i] and not visited[i]:
            dfs(i, visited, computers) #정점 i의 이웃노드 탐색을 위해 dfs() 호출

def solution(n, computers):
    answer = 0 #네트워크의 갯수
    visited = [False] * n #방문여부 확인

    #각 점마다 확인해야 하기 때문에!
    for i in range(n): #전체 노드를 확인하기 위해서 / for를 사용했기 떄문에 자연스럽게 i를 늘려가면서 노드를 이동할 수 있네!
        if not visited[i]: #아직 방문하지 않은 정점이면
            dfs(i, visited, computers) #드가자!
            answer += 1 #하나의 네트워크를 찾았다
    return answer



#bfs 풀이

from collections import deque

def bfs(root, visited, computers):
    visited[root] = True #방문처리
    q = deque() #큐 생성
    q.append((root)) # 초기값 생성
    while q:
        now = q.popleft() #값 빼고
        for i in range(len(computers)): #그 값을 검증
            #방문하지 않은 컴퓨터가 있고, 방문하지 않은 곳 이라면,
            if computers[now][i] and not visited[i]:
                visited[i] = True
                q.append(i) # 갈 수 있으니 큐에 넣은 것!



def solution(n, computers):
    answer = 0 #네트워크의 갯수
    visited = [False] * n #방문여부 확인

    #각 점마다 확인해야 하기 때문에!
    for i in range(n): #전체 노드를 확인하기 위해서 / for를 사용했기 떄문에 자연스럽게 i를 늘려가면서 노드를 이동할 수 있네!
        if not visited[i]: #아직 방문하지 않은 정점이면
            bfs(i, visited, computers) #드가자!
            answer += 1 #하나의 네트워크를 찾았다
    return answer