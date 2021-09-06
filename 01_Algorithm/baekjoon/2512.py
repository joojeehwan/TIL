'''



상한액을 어떻게 잡을까?!

이거 이진탐색으로 풀어야 한다,,! 


=> 
다른 수학적 논리가 아니다! 


인덱스로도 풀어보자아,,,토요일에,,,


'''



N = int(input())

budgets = list(map(int, input().split()))

total_budgets = int(input())

start, end = 0, max(budgets) #0으로 설정해야해,,,



while start <= end: #종료조건! 

    mid = (start + end) // 2
    total = 0
    for budget in budgets:
        if budget > mid:
            total += mid
        else:
            total += budget
    if total <= total_budgets:
        start = mid + 1 # 더 큰 상한액을 찾기 위해서! => mid값을 조정 
    else:
        end = mid - 1 # 더 작은 상한액을 찾기 위해서! => mid값을 조정 
print(end)
