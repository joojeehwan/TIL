#dfs 정리

#수업

# def dfs(s, v):
#     visted = [0] * (v+1)
#     stack = [s]
#     i = s #현재 방문한 정점 i
#     visted[i] = 1
#     print(node[i])
#     while i != 0: # True:
#         for w in range(1, v+1):
#             if adj[i][w] == 1 and visted[w]==0:
#                 stack.append(i)
#                 i = w
#                 visted[w] = 1
#                 print(node[i])
#                 break
#         else:
#             if stack: 
#                 i = stack.pop(-1)
#             else:
#                 i = 0



# adj = [[0,0,0,0,0,0,0,0], 
#         [0,0,1,1,0,0,0,0],
#         [0,1,0,0,1,1,0,0],
#         [0,1,0,0,0,1,0,0],
#         [0,0,1,0,0,0,1,0],
#         [0,0,1,1,0,0,1,0],
#         [0,0,0,0,1,1,0,1],
#         [0,0,0,0,0,0,1,0]]

# node = ["", "A", "B", "C", "D", "E" ,"F", "G"]
        
# # dfs(1,9)


# #재귀로 dfs


# def dfs_3(graph, v, visted):
#     viseted[v] = True
#     print(v, end = "")
#     for i in graph[v]:
#         if not visted:
#             dfs(graph, i, visted)
                   
# visted = [False] * 9

# graph = [[],
#         [2,3,8],
#          [1,7],
#          [1,4,5],
#          [3,5],
#          [3,4],
#          [7],
#          [2,6,8],
#          [1,7]
#             ]



#담당교수님식 dfs 풀이 => 주로 모든 방법을 다 해봐야 하는 경우에 많이 사용! 


visted = [0] * (8) #노드의 갯수보다 하나 많아야 함!
prev = [0] * 8 # <- 누구를 통해서 왔는가?
counts = [0] * 8 #<- A로부터 얼마나 가야되는가?
def dfs2(now): 

  
    #2 옵션 (기저조건, 문제에 따라 특이한 끝날 조건)
    print(node[now])

    #1. 현재 now에서 갈 수 있는 next를 찾아서 가라!
    for i in range(1,8):
        if adj[now][i] == 1 and visted[i] == 0:
            next = i
            visted[next] = 1
            counts[next] = counts[now] + 1
            prev[next] = now
            dfs2(next)

    #3. 문제가 생길 수 있는 부분(Error발생 가능한 부분들 수정)
    #4. 계산 및 추가 작업

#          A  B  C  D  E  F  G
adj = [[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 0, 0], # A
       [0, 1, 0, 0, 1, 1, 0, 0], # B
       [0, 1, 0, 0, 0, 1, 0, 0], # C
       [0, 0, 1, 0, 0, 0, 1, 0], # D
       [0, 0, 1, 1, 0, 0, 1, 0], # E
       [0, 0, 0, 0, 1, 1, 0, 1], # F
       [0, 0, 0, 0, 0, 0, 1, 0]] # G
node = ['', 'A','B','C','D','E','F','G']

visted[1] = 1
dfs2(1)



#dfs 2차원 배열에 적용


def dfs_2nd (row, col): # now : row, col의 위치

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):
        next_row = row + dr[i]
        next_col = row + dc[i]
        #now -> next로 갈 수 있으면 가라! 

        #근데 맵을 벗어나는 경우를 확인하라! 
        if next_row < 0 or next_col < 0 or next_row >=h or next_col >= w:
            continue
        
        if MAP[next_row][next_col] == 1 and visted[next_row][next_col] == 0:
            #인접해 있는 육지이고, 가본 적이 없는 곳이라면 간다!
            visted[next_row][next_col] = 1
            dfs(next_row, next_col)



while True:
    w, h  = map(int, input().split())
    if w == 0 and h == 0:
        break

    MAP = [list(map(int, input().split())) for _ in range(h)]
    visted = [[0] * w for _ in range(h)]
     # visited[row][col] <- 1 : row,col을 들린적있다. 0 : row, col를 들린적 없다.
    for i in range(h):
        for j in range(w):
            if MAP[i][j] == 1 and visted[i][j] == 0:
                visted[i][j] = 1
                dfs_2nd(i, j)
            
