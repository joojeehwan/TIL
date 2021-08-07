"""
1970: 쉬운 거스름돈
"""

import sys
sys.stdin = open('1970_input.txt')




T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    count = 0
    coin_types = [50_000, 10_000, 5_000, 1_000, 500, 100, 50, 10]
    res = []
    for coin in coin_types :
        res.append(N // coin)
        if N >= coin :
            N %= coin

    print(f"#{tc}\n{' '.join(map(str, res))}")



    

