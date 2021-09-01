"""
1219: 길찾기
"""

import sys
sys.stdin = open('1219_input.txt')

#인접행렬 풀이

# def DFS_2(now):
#     global ans

#     #베이스 조건
#     if now == 99:
#         ans =1
#         return
    
#     visited[now] = 1

#     for w in range(100):
#         if visited[w] == 0 and adj_arr[now][w] == 1: #한번도 안 가본 곳이고, 연결된 곳이라면!
#             DFS_2(w)




# for _ in range(10):


#     tc, N = map(int, input().split())

#     road = list(map(int, input().split()))


# #인접 행렬

# #이런 입력도,,,!
#     adj_arr = [[0] * 100 for _ in range(100)]

#     for i in range(N):
#         adj_arr[road[2*i]][road[2*i+1]] = 1


    
#     visited = [0] * 100
#     ans = 0
#     DFS_2(0)

#     print("#{} {}".format(tc, ans))


#인접 리스트 풀이 => 이것이 바로 이코테 입력! 





for tc in range(10):

    tc, N = map(int, input().split())

    load = list(map(int, input().split()))

    adj_lst = [[] for _ in range(100)]

    for i in range(N):  #번호가 노드이고, 그 노드를 확정하고 append 갈 수 있는 노드들을 표시
        adj_lst[load[2*i]].append(load[2*i+1])




    visited = [0] * 100
    ans = 0
    stack = [0]


    while stack :
        now = stack.pop()

        if now == 99:
            ans = 1
            break
    
        if visited[now]: 
            continue

        visited[now] = 1

        for w in adj_lst[now]:
            if not visited[w]: #여기서는 연결되어 있는 친구들만 알짜배기로 가져와서 굳이 연결의 유무를 확인할 필요가 없다! 
                stack.append(w)

    print("#{} {}".format(tc, ans))


        