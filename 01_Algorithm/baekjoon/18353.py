'''

LIS 문제


# 11053번
x = int(input())

arr = list(map(int, input().split()))

dp = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

'''

#a[i]의 값이 더 작은 경우에 dp의 값을 배정해 줬다는 것
n = int(input())

lst = list(map(int, input().split()))

dp = [1] * n


for i in range(n):
    for j in range(i):
        if lst[i] < lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)


print(len(lst) - max(dp))
