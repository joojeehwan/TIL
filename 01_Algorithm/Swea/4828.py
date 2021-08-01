"""
4828: min - mix
"""

import sys
sys.stdin = open('4828_input.txt')



def min_max(n, numbers):

    max_num = numbers[0]
    min_num = numbers[0]


    for i in range(n):
        if max_num < numbers[i]:
            max_num = numbers[i]

        elif min_num > numbers[i]:
            min_num = numbers[i]

    
    return max_num - min_num

    
    





T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    n_list = list(map(int, input().split()))

    print(f"#{tc} {min_max(N, n_list)}")