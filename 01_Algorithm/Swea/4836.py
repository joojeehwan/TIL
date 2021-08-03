"""
4836: 색칠하기
"""

import sys

sys.stdin = open('4836_input.txt')



#def sol (n, lst1, lst2):

lst1 = [2,2,4,4]
lst2 = [3,3,6,6]

res = (lst1[2] - lst2[0] + 1) * (lst1[3] - lst2[1] + 1)

print(res)