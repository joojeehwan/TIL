"""
4843: 특별한 정렬
"""

import sys
sys.stdin = open('4843_input.txt')



#최대값을 구하고, 팝해서 리스트에 넣기를 반복,,!
#정렬을 하고

def sol(n, lst):
    res = []
    sorted_lst = sorted(lst, reverse=True)

    for _ in range(0, 5):
        res.append(sorted_lst.pop(0))
        res.append(sorted_lst.pop(len(sorted_lst) - 1))

    return res
   

T = int(input())

for tc in range(1, T + 1):
    print()
    N = int(input())

    lst = list(map(int, input().split()))

    for num in sol(N, lst):
        print(f"#{tc}", end=" ")
        print(num, end=" ")
