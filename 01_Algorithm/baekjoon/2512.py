'''



상한액을 어떻게 잡을까?!

이거 이진탐색으로 풀어야 한다,,!




'''



N = int(input())

budgets = list(map(int, input().split()))

total_budgets = int(input())

start, end = 0, max(budgets)



while start <= end:

    mid = (start + end) // 2
    total = 0
    for budget in budgets:
        if budget > mid:
            total += mid
        else:
            total += budget
    if total <= total_budgets:
        start = mid + 1
    else:
        end = mid - 1
print(end)
