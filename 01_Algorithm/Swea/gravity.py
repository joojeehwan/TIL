
import sys
"""
Baby_Gin: Baby Gin
"""

import sys
sys.stdin = open('gravity_input.txt')


tc = int(input())

for t in range(1, tc +1):
    N = int(input())
    Height = list(map(int, input().split()))
    res = []
    for j in range(0, len(Height)):
        cnt = 0
        for i in range(1, N):
            if Height[j] > Height[i]:
                cnt += 1
        res.append(cnt)

    maxv = res[0]
    for i in res:
        if maxv < i:
            maxv = i

    print(f"#{t} {maxv}")
