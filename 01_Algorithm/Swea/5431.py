"""
5431: 민석이의 과제 체크하기
"""

import sys
sys.stdin = open('5431_input.txt')


def sol (n, li):

    res = []
    for i in range(1, n+1):
        res.append(i)
        for j in li:
            if res.count(j) != 0:
                res.remove(j)
    return res


T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    my_list = list(map(int, input().split()))
    
    print()
    print(f"#{tc} " ,end="")
    for i in sol(N, my_list):
        print(i, end=" ")
        
       