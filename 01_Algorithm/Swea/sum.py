"""
sum: sum
"""

import sys
sys.stdin = open('sum_input.txt')

T = 10

for tc in range(1, T+1):

    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(100)]

    res = []

    #행 합
    for i in range(len(lst)):
        sum_row = 0
        for j in range(len(lst[i])):
            sum_row += lst[i][j]
        res.append(sum_row)

    # 열 합
    for j in range(len(lst[0])):
        sum_col = 0
        for i in range(len(lst)):
            sum_col += lst[i][j]
        res.append(sum_col)
    # 대각선 합
    sum_dia = 0
    for i in range(len(lst)):
        sum_dia += lst[i][i]
    res.append(sum_dia)
    # 역 대각선 합

    sum_revesr_dia = 0

    for i in range(len(lst)):
        sum_revesr_dia += lst[i][99-i]

    res.append(sum_revesr_dia)

    max_val = 0
    for i in range(len(res)):
        if max_val < res[i]:
            max_val = res[i]

    print(f"{tc} {max_val}")