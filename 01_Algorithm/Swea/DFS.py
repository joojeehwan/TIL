#dfs 정리

#수업

def dfs(s, v):
    visted = [0] * (v+1)
    stack = [s]
    i = s #현재 방문한 정점 i
    visted[i] = 1
    print(node[i])
    while i != 0: # True:
        for w in range(1, v+1):
            if adj[i][w] == 1 and visted[w]==0:
                stack.append(i)
                i = w
                visted[w] = 1
                print(node[i])
                break
        else:
            if stack: 
                stack.pop(-1)
            else:
                i = 0



adj = [[0,0,0,0,0,0,0,0], 
        [0,0,1,1,0,0,0,0],
        [0,1,0,0,1,1,0,0],
        [0,1,0,0,0,1,0,0],
        [0,0,1,0,0,0,1,0],
        [0,0,1,1,0,0,1,0],
        [0,0,0,0,1,1,0,1],
        [0,0,0,0,0,0,1,0]]

node = ["", "A", "B", "C", "D", "E" ,"F", "G"]
        
dfs(1,9)


#재귀로 dfs


def dfs(graph, v, visted):
    viseted[v] = True
    print(v, end = "")
    for i in graph[v]:
        if not visted:
            dfs(graph, i, visted)
                   
visted = [False] * 9

graph = [[],
        [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]
            ]


                             
                      