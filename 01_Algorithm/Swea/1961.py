

"""
1961: 숫자 배열 회전
"""

# import sys
# sys.stdin = open('1961_input.txt')

T = int(input())

for tc in range(1, T+1):
    
    N = int(input())

    lst= [input().split() for _ in range(N)]

    res = []
  
    print(lst)

    #90도
    for j in range(len(lst)):
        print()
        for i in range(len(lst)-1 ,-1, -1):
            print(lst[i][j], end = "")

    #180도
    for i in range(len(lst)-1, -1, -1):
        print()
        for j in range(len(lst)-1, -1, -1):
            print(lst[i][j], end ="")


    #270도

    for i in range(len(lst)-1, -1, -1):
        print()
        for j in range(len(lst)): 
            print(lst[j][i], end ="")