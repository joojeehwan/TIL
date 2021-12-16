'''

특정 거리의 도시 찾기


BFS 문제! 정확히!

'''

'''

도시의 개수 : N
도로의 개수 : M
거리 정보 : K
출발 도시의 번호 : X

'''
from collections import deque
N, M, K, X = map(int, input().split())


#1. 그래그 구성하기

#N + 1의 이유?! => 우리는 1번 노드 부터 생각한다.
MAP = [[] for _ in range(N + 1)]

for _ in range(M):
    frm,to = map(int, input().split())
    MAP[frm].append(to)


#2. 큐  / 거리 배열 생성 
    
q = deque([X])
'''
q = deque()
q.append(X)
와 같은데 한번에 적으면 위에 처럼 된다
'''

#모든 도시에 대한 최단 거리 초기화
distance = [-1] * (N + 1)


#3. 시작점 세팅
#출발하는 도시의 경우 거리 0으로 설정
distance[X] = 0
#q.append([X])


#print(q)

#BFS실행
#규 생성


while q:

    #1. q에서 맨앞점을 꺼내기!
    now = q.popleft()
    
    #현재 도시에서 이동 할 수 있는 모든 도시를 확인

    for next in MAP[now]:
        #아직 방문하지 않은 도시라면
        if distance[next] ==  -1:
            #최단거리 갱신
            distance[next] = distance[now] + 1
            q.append(next)

#최단 거리가 K인모든 도시의 번호를 오름차순으로 출력

#최단거리가 K인것이 없을떄를 대비한 falg
check = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        #최단거리가 k인 도시가 있는 것!
        check = True
        

#만약 최단 거리가 K인 도시가 없다면, -1를 출력하도록
if check == False:
    print(-1)


