"""
4834: 숫자카드
"""

import sys
sys.stdin = open('4834_input.txt')



def sol(numbers):

    #카드와 그 갯수를 담는 dict갯수 생성

    num_dict = {}
    for num in numbers:
        num_dict[num] = numbers.count(num) 


    max_val = 0
    max_key = []

    for key, val in num_dict.items():
        if val >= max_val:
            max_val = val
            max_key.append(key)

    result = str(max(max_key)) + " " + str(max_val)

    
    return result





T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))

    print(f"#{tc} {sol(numbers)} ")



def count_n(n): 
    lst = [0] * 10 # 0~9까지 저장용
    result = 0
    for i in n: # 
        lst[int(i)] += 1 # 나온 값 카운팅
    max_n = 0
    for i in range(10):
        if lst[i] >= max_n: #수가 같으면 큰값이 나와야 하므로 >= 이용
            max_n = lst[i]   # 가장 많이 나온 횟수
            result = i       # 그때 값
    return result, max_n

num = int(input())
for i in range(num):
    number = int(input())
    n = input()
    result = count_n(n)
    print(f'#{i+1} {result[0]} {result[1]}')