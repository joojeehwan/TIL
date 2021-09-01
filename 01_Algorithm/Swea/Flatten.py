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

        #직접적인 덤프질! 
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
    




T = 10
for tc in range(T):
    dumps = int(input())
    boxes = list(map(int, input().split()))

    # counts 리스트 만들기
    # 어떤 높이가 몇 개 있는지 세어둔 리스트
    counts = [0] * 101
    # index : 높이, value : 해당 높이가 몇 개 있는가?
    max_height = 0 # 최대 높이
    min_height = 101 # 최소 높이
    for box in boxes:
        counts[box] += 1
        if max_height < box :
            max_height = box
        if min_height > box :
            min_height = box

    for i in range(dumps):
        counts[max_height] -= 1
        counts[max_height - 1] += 1
        counts[min_height] -= 1
        counts[min_height + 1] += 1
        if counts[max_height] == 0:
            max_height -= 1
        if counts[min_height] == 0:
            min_height += 1

    ans = max_height - min_height
    print("#{} {}".format(tc + 1, ans))