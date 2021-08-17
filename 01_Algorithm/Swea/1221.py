"""
1221: GNS
"""

import sys
sys.stdin = open('GNS_test_input.txt')



T = int(input())

for tc in range(1, T+1):

#counts 배열을 만들어서 푸는데,,, 숫자가 아니라서 약간의 스킬이 필요함!

    num, amount  = input().split()
    data = list(input().split())
    ori = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    counts = [0] * len(ori)

    for now in data:
        num = -1
        for i in range(10):
            if now == ori[i]:
                num = i  

        counts[num] += 1
    # print()
    print(f"#{tc}")
    for i in range(len(ori)):
        for _ in range(0, counts[i]):
                
            print(ori[i] , end=" ")
    print("")