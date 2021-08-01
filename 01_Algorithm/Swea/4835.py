"""
4835: 문제명을 입력해주세요 :)
"""

import sys
sys.stdin = open('4835_input.txt')


prefix_sum = [0]

def prefix_sum(n, m, data):

    sum_value = 0
    prefix_sum = [0]
    for i in data:
        sum_value += i 
        prefix_sum.append(sum_value)

    
    res = []
    for i in range(0,  n - m + 1): #저렇게 이동,,! 

        res.append(prefix_sum[i + m] - prefix_sum[i])
    
    max_val = res[0]
    min_val = res[0]

    for re in res:
        if re > max_val:
            max_val = re
        elif re < min_val:
            min_val = re

    return max_val - min_val         

    


TC = int(input())

for tc in range(1, TC+1):

    N, M = map(int, input().split())

    data = list(map(int, input().split()))

    print(f"#{tc} {prefix_sum(N, M, data)}")