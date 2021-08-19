



def dfs(now): #now : 나의 현재 위치


    #2 기저조건 (옵션)

    #1 now에서 갈 수 있는 next찾기

    for to in range(V+1):
        if adj[now][to] == 1 and visted[to] == 0:
            visted[to] = 1
            dfs(to)


    
T = int(input())

for tc in range(1, T+1):

    V,E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    visted = [0] * (V+1) #들렸던 점인가?
    #adj[from][to]

    for i in range(E):
        f, t = map(int, input().split())
        # f : 어디에서 

        
        # t : 어디로
        adj[f][t] = 1

    start, end = map(int, input().split())
    visted[start] = 1
    dfs(start) # start에서부터 갈 수 있는 모든 곳으로 전부 가보게 된다.
    print("#{} {}".format(tc + 1, visted[end])) # <- 갔던 점인가?
