



"""
12586: 회문
"""

# import sys
# sys.stdin = open('12586_input.txt')



T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    str_list = [input() for _ in range(N)]

    for i in range(N):
 
        temp = ""
        for j in range(N):
            temp += str_list[j][i]
        str_list.append(temp)

    ans = ""


    for str_temp in str_list:
        for i in range(N-M+1):
            temp = str_temp[i:i + M]
            
            #회문 : 앞에서 부터 읽은 문자열 == 뒤에서 부터 읽은 문자열
            cnt = 0

            for j in range(len(temp) // 2):
                if temp[j] == temp[len(temp) -1 -j]:   
                    cnt += 1
            if cnt == len(temp) // 2: 
                ans = temp


print("{} {}".format(tc + 1, ans))





T = int(input())

for tc in range(1, T+1):

    N, M = map(int(input().split()))
    str_lst = [input() for _ in range(N)]

    for i in range(N):

        temp = ""

        for j in range(N):
            temp += str_list[j][i]
        str_list.append(temp)

    ans = ""
    for str_temp in str_list:
        for i in range(N - M + 1):
            temp =  str_temp[i:i+M] #글자 하나씩 비교하는 거니깐!
            cnt = 0
            for j in range(len(temp) // 2):
                if temp[j] == temp[len(temp) -1 -j]:
                    cnt += 1
            if cnt == len(temp) // 2:
                ans = temp




#그냥 몸통 박치기 풀이!



for tc in range(T):
    N, M = map(int, input().split())
    str_lst = [input() for _ in range(N)]
    ans = ""
    for row in range(len(str_lst)):

        #가로
        for col in range(N-M+1):
            temp = str_lst[row][col:col + M]
            cnt = 0

            for j in range(len(temp) // 2):
                if temp[j] == temp[len(temp) - 1 -j]:
                    cnt += 1

            if cnt == len(temp) // 2:
                ans = temp

        #세로
        for col in range(N-M+1):
            cnt = 0
            for j in range(M // 2):
                if str_list[col + j][row] == str_list[col + M -1 -j][row]:
                    cnt += 1
            if cnt == M // 2:
                ans =temp

            
        