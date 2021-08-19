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
        temp = "" #여기에 있는 거 포인트! 여기에 있으면서 
        for j in range(100):
            temp += str_lst[j][i]
        
        str_lst.append(temp) #이렇게 추가


    ans = ""
    max_ans = 0
    for str_temp in str_lst:
        for i in range(100+1):
            for j in range(i+1,100+1):
                temp = str_temp[i:j]

                cnt = 0
                for j in range(len(temp) // 2): # //2 없어도 가능
                    if temp[j] == temp[len(temp)-1-j ]:
                        cnt += 1
                if cnt == len(temp) // 2: # // 2 없어도 가능
                    ans = temp
                
                if  max_ans <= len(ans):
                    max_ans = len(ans)

    print(f"#{N} {max_ans}")




#교수님 풀이

T = 10

for tc in range(T):
    N = int(input())
    size = 100
    str_lst = [input() for _ in range(size)]


    for i in range(size):
        temp = ""
        for j in range(size):
            temp += str_lst[j][i]

        str_lst.append(temp)


    
    ans = 0
    flag = 0 #찾았는가?

    for M in range(size, 1, -1):
        for str_temp in str_lst:
            for i in range(size - M + 1):
                temp = str_temp[i: i + M]

                cnt = 0
                for j in range(len(temp)):
                    if temp[j] == temp[len(temp) -1 -j]:
                        cnt += 1

                if cnt == len(temp):
                    ans = M
                    flag = 1





                
