"""
4466: 최대 성적표 만들기
"""

import sys
sys.stdin = open('4466_input.txt')


def max_grade_card(lst,k):

    sorted_lst = sorted(lst, reverse=True)

    sum = 0

    for i in range(0, k):
        sum += sorted_lst[i]

    return sum

    



T = int(input())

for tc in range(1, T + 1):

    N, K = map(int, input().split())

    my_lst = list(map(int, input().split()))

    print(f"#{tc} {max_grade_card(my_lst, K)}")





    
