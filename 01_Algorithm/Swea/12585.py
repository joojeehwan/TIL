"""
12585: 문자열 비교
"""

import sys
sys.stdin = open('12585_input.txt')

T = int(input())


for tc in range(1, T+1):

    str1 = input()
    str2 = input()
    flag = 0



    for i in range(len(str2) - len(str1) + 1):
#문자하나가 참일때 마다 cnt를 증가시키면 전체길이와 그 cnt를 비교하면 전체 비교가 가능! 
        cnt = 0 #하나씩 비교하기 때문에 필요! 전체를 다 하는게 아니라서! 길
        for j in range(len(str1)):
            if str1[j] == str2[i + j]:
                cnt += 1
            
        if cnt == len(str1):
            flag = 1
        
    print("#{} {}".format(tc + 1, flag))