"""
1216: 회문2
"""

import sys
sys.stdin = open('1216_input.txt')



#가장 긴 회문의 길이를 구하라! 
'''


어떻께 해야 할까,, 

한줄에 있는 모든 길이를 탐색하고, 가장 긴 길이의 회문을 저장하면 돼!



'''
T = 10

for tc in range(1, T+1):
    
    N = int(input())
    str_lst = [input() for _ in range(100)]

    for i in range(100):
        temp = ""
        for j in range(100):
            temp += str_lst[j][i]
        
        str_lst.append(temp)


    ans = ""
    max_ans = 0
    for str_temp in str_lst:
        for i in range(100+1):
            for j in range(i+1,100+1):
                temp = str_temp[i:j]

                cnt = 0
                for j in range(len(temp) // 2):
                    if temp[j] == temp[len(temp)-1-j ]:
                        cnt += 1
                if cnt == len(temp) // 2:
                    ans = temp
                
                if  max_ans <= len(ans):
                    max_ans = len(ans)

    print(f"#{N} {max_ans}")
                
