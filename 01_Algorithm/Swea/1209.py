

"""
1209: [s/w 문제해결 기본]2일차 - Sum
"""

import sys
import pprint
sys.stdin = open('1209_input.txt')


def max_sum(num_li):

    true_max = 0
    for i in range(100):
   
        max_hor = 0
        max_ver = 0
        max_dia_1 = 0
        max_dia_2 = 0
        for j in range(100):
            max_hor += num_li[i][j]
            max_ver += num_li[i][j]

            #가로 / 세로 줄의 합 중 "최댓값이 나오면 갱신"
        if max_hor > true_max:
            true_max = max_hor
        if max_ver > true_max:
            true_max = max_ver

        max_dia_1 += num_li[i][i]
        max_dia_2 += num_li[i][len(num_li) - 1 - i]

        if max_dia_1 > true_max:
            true_max = max_dia_1  
        if max_dia_2 > true_max:
            true_max = max_dia_2


        return true_max







T = 10

for tc in range(1, T+1):
    test_number = int(input())
    my_matrix = []

    # input 값으로 2차원 배열 만들기
    for i in range(100):
        my_matrix.append(list(map(int, input().split())))

    print(f'#{tc} {max_sum(my_matrix)}')

