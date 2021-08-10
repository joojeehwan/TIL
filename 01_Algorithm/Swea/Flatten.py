"""
Flatten: Flatten
"""

import sys
sys.stdin = open('Flatten_input.txt')




#가장 큰 값에서 1빼고, 가장 작은 값 1 더하고 => 덤프


T = 10
for tc in range(1, T+1):

    N = int(input())
    res = list(map(int, input( ).split()))

    for _ in range(N):

        max_val_idx = res[0]
        min_val_idx = res[0]

        for i in range(len(res)):

            if res[max_val_idx] < res[i]:

                max_val_idx  = i

            if res[min_val_idx] > res[i]:

                min_val_idx = i

        res[max_val_idx] = res[max_val_idx] - 1
        res[min_val_idx] = res[min_val_idx] + 1

        # print(res)
        # print(res[max_val_idx], res[min_val_idx])
        

    max_val = res[0]
    min_val = res[0]
        
    for i in range(len(res)):

        if max_val < res[i]:
            max_val = res[i]
        if min_val > res[i]:
            min_val = res[i]

    print(f"#{tc} {max_val - min_val}")
    




