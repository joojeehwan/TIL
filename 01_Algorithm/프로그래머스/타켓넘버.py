
ans = 0

def dfs(lev, SUM, lst, goal):
    global ans
    N = len(lst)

    if lev == N:
        if goal == SUM:
            ans += 1
            return
    else:
        dfs(lev + 1, SUM + lst[lev], lst, goal)
        dfs(lev + 1, SUM - lst[lev], lst, goal)


count = 0

'''

둘의 차이 return 의 위치 제대로 파악하기! 

'''

def dfs(idx, value, numbers, target):
    # 전역변수 count 사용 선언
    global count
    length = len(numbers)
    # 재귀함수 base case
    # 문제가 충분히 작아서 바로 풀수 있는 경우
    # return으로 함수 종료를 해줘야함
    if idx == length:
        if value == target:
            count += 1
        return

        # 재귀함수 recursive case
    # 재귀적으로 부분 문제를 푸는 경우.
    dfs(idx + 1, value + numbers[idx], numbers, target)
    dfs(idx + 1, value - numbers[idx], numbers, target)


from collections import deque


def solution(numbers, target):
    ans = 0
    q = deque()
    n = len(numbers)
    q.append((0, 0))
    while q:
        now_sum, index = q.popleft()
        if index == n:
            if now_sum == target:
                ans += 1

        else:
            q.append((now_sum + numbers[index], index + 1))
            q.append((now_sum - numbers[index], index + 1))

    return ans

def solution(numbers, target):
    global count
    dfs(0, 0, numbers, target)

    return count




def solution(numbers, target):
    global ans
    dfs(0, 0, numbers, target)
    return ans