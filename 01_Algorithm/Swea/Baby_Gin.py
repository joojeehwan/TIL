import sys
"""
Baby_Gin: Baby Gin
"""

import sys
sys.stdin = open('Baby_Gin_input.txt')




#탐욕 알고리즘으로

T = int(input())

for tc in range(1, T + 1):
    cards = int(input())

    counts = [0] * 10

    for _ in range(6):
        counts[cards % 10] += 1
        cards //= 10


    i = 0
    tri = run = 0

    while i < 8:
        if counts[i] >= 3 :
            counts[i] -= 3
            tri += 1
            continue #이것이 있어야지

        if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1 :
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
            run += 1
            continue
        i += 1
    if run + tri == 2 : print("#{} Baby Gin".format(tc))
    else :  print("#{} Lose".format(tc))


