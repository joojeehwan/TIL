'''


소수 구하기


힌트 : 에라토스테네스의 체

에라토스테네스의 체

1. 2부터 N까지의 모든 자연수를 나열한다.
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
3. 남은 수 중에서 i의 배수를 모두 제거한다(i는 제거하지 않는다)
4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복.


'''



# import math
#
# n = 120
#
# array = [True for i in range(n + 1)] #처음엔 모든 수가 소수인 것으로 초기화 0과 1 제외
#
#
#
# #에라토스테네스의 채 알고리즘
#
#
# for i in range(2, int(math.sqrt(n))+1):
#     if array[i] == True: #i가 소수인 경우
#
#     #i를 제외한 i의 모든 배수를 지우기
#         j = 2
#         while i * j <= n :
#             array[i*j] = False
#             j += 1
#
# for i in range(2, n+1):
#     if array[i]:
#         print(i, end = " ")






# M, N  = map(int, input().split())
#
# array = [True for i in range(N + 1)]
#
# for i in range(M):
#     array[i] = False
#
# for i in range(M, int(math.sqrt(N)) + 1): #배수들을 지워가는거 이기 때문에 N의 제곱근 보다 작은 배수들만 지워도 충분!
#     if array[i] == True:
#         j = 2
#         while i * j <= N:
#             array[i*j] = False
#             j += 1


#아 위에 식으로 하면 2의 배수가 안지워지네,,?! 3 하고  16을 넣었는데!?
# 아 그러면 일단 에라토스테네스의 채를 하고! 그 다음에 마지막 부분을 건드려야 하네!
import math

M, N = map(int, input().split())

array = [True for _ in range(N + 1)] #처음엔 모든 수가 소수인 것으로 초기화 0과 1 제외
array[0] = False
array[1] = False
#에라토스테네스의 채 알고리즘


for i in range(2, int(math.sqrt(N))+1):
    if array[i] == True: #i가 소수인 경우

    #i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= N :
            array[i*j] = False
            j += 1



for i in range(M, N+1):
    if array[i]:
        print(i)

#아 ,,1은 소수가 아닌데 나오네? 1의 경우를 확인하자!


# 와 이거 왜 자꾸 런타임오류 뜨지,,?! 다르게 풀어봐야 겠다!

#와 임포트 매스를 안해서,,,


#소수를 판별하는 함수를 만들어보자!


# def is_prime(num):
#
#     if num == 1 :
#         return False
#
#     else:
#         for i in range(2, math.sqrt(math) + 1):
#             if num % i == 0:
#                 return False
#
#             else:
#                 return  True