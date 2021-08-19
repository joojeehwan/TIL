"""
2005: 파스칼의 삼각형
""" 

# import sys
# sys.stdin = open('2005_input.txt')


# #전혀 몰랐음


'''

구하고 싶은 값 <- 그 구하고 싶은 값이 변할 수 있는 요인
=> 위치 -> 2가지 "줄" / "칸"

저장할 공간 <- dp["줄"]["칸"]

배열의 차원 : 변인 요인의 개수

한번 계산한 값은 변하지 않는다...

앞에서 저장된 어떤 값을 가져올ㅈ..

현재라고 가정을 하고 내 앞에 어떤 애들이 필요한가?!

'''


T = int(input())



for tc in range(1, T+1):

    N = int(input())

    lst = [[0] * i for i in range(1,N+1)]


    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if i == j :
                lst[i][j] = 1

            elif j == 0:
                lst[i][j] = 1

            else:
                lst[i][j] = lst[i-1][j-1] + lst[i-1][j]

    print(f"#{tc}", end="")
    for i in range(len(lst)):
        print()
        for j in range(len(lst[i])):
            print(lst[i][j], end=" ")
            





#dfs

dp = [[0] * 1000 for _ in range(100)]

dp[0][0] = 1

for row in range(1, 100):
    for col in range(100):
        dp[row][col] = dp[row-1][col-1] + dp[row-1][col]


T = int(input())

for tc in range(T):
    N = int(input())
    print(f"{tc}")
    for row in range(N):
        for col in range(row+1):
            print(f"{dp[row][col]}", end="")
        print("")