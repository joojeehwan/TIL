'''

연산자 끼워넣기

브루트포스로 풀거나 아니면 백트래킹(dfs)를 써서 풀라함,,힌트에선

dfs로 풀수가 있는 건가?! dfs는 잘 모르는데! 다시 공부하러,,!

으렵다,,,,,,,,

주사위 복습하고 다시 풀어보자!

'''

'''

백트래킹 문제.
백트래킹은
1) 종료조건
2) 원하는 값
3) 분기

세 개를 잘 구현해야 함

1) 종료조건 : Day > N. 퇴사일 넘어서 일할 때
2) 원하는 값: max profit
3) 분기:
(1) 일을 하기로 할 때
    '날짜' 변수에는 일 할때 걸리는 시간
    'profit' 변수에는 일 하고 나서 받는 돈
    넣고 재귀

(2) 일을 하지 않을 때
    일을 하지 않더라도 날짜는 하루 지나가므로
    '날짜+1' 더해서 재귀
'''

"""
# 주사위를 N번 던져서 나올 수 있는 눈의 조합
# 단, 같은 눈을 2번이상 뽑으면 안된다!
# 1 1 ???
# N = 3
# path = [-1] * N

# DAT = [0] * 7
# sum = 0
# cnt = 0
#
#
# def dfs(now):
#     global sum
#     global cnt
#     if now >= N:
#         # N개의 주사위를 전부 뽑았다.
#         print(path, sum)
#         return
#     # DAT[index] -> index : 주사위눈, value : 해당 주사위 눈을 뽑은적이 있는가?
#
#     # now : 몇 번째 주사위를 던질 것인가?
#     # 1, 2, 3, 4, 5, 6
#     for i in range(1, 7):
#         # i라는 눈을 뽑았다.
#         path[now] = i # now번째에 i라는 눈을 뽑았다 라고 기록
#         sum += i
#         cnt += 1
#         # i라는 눈을 뽑았을 때, 다음 주사위 눈도 뽑으러 가라!
#         dfs(now + 1)
#         sum -= i
#         cnt -= 1
#         path[now] = -1 # i라는 눈을 뽑았을 때 방법들은 끝났으니 복구
#
# dfs(0)


"""





#재귀함수 이해할 수 있는,,, 좋은 문제!!

N = int(input())

nums = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

MIN , MAX = 1e9, -1e9 #최대 최소를 문제에 주어진 10억으로,,!



def dfs (now, res):

    global add, sub, mul, div
    global MIN
    global MAX
    if now == N: #  N개의 수를 다 뽑았다.
        MAX = max(res, MAX)
        MIN = min(res, MIN)
        return

    # +
    if add:
        add -= 1 #+를 사용하니깐 빼고!
        dfs(now+1, res+nums[now])
        add += 1 #끝까지 가고 다시 돌아와서 처음 부터!

    # -
    if sub:
        sub -= 1
        dfs(now+1, res-nums[now])
        sub += 1

    # *
    if mul:
        mul -= 1
        dfs(now + 1, res * nums[now])
        mul += 1

    if div:
        div -= 1
        dfs(now+1, int(res/nums[now]))
        div += 1

dfs(1, nums[0])
print(MAX)
print(MIN)



#함수에서 change 배열은 괜찮아!
# arr = [1,2,3,4]
# num = 4
#
# def arr_change(arr):
#
#     arr[0] = 10
#     num = 6
#     return arr, num
#
# print(arr_change(arr))
#
# print(arr)
# print(num)
