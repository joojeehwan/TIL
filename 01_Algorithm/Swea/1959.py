

"""
1959: 
"""

import sys
sys.stdin = open('1959_input.txt')


def multiply_max(lst1, lst2):

    maxi = 0
    for i in range(len(lst2) - len(lst1) + 1):
        temp = 0

        for j in range(len(lst1)):
            temp += lst1[j] * lst2[i + j]
        if maxi < temp:
            maxi = temp
    return maxi


test_case = int(input())


for tc in range(1, test_case + 1):
    first, second = map(int, input().split())

    first_lst = list(map(int, input().split()))

    second_lst = list(map(int, input().split()))

    if first > second:
        ans = multiply_max(second_lst, first_lst)
    else:
        ans = multiply_max(first_lst, second_lst)

    print(f'#{tc} {ans}')

