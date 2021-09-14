'''


퇴사



오 이거 어떻게 해야 되지,,?!

다이나믹? 프로그래망?? 헐,,

이런거 생각하지 진짜 어렵구만,,,
'''




#피보나치 수열
#이걸 잘할 수 있다면 다른 dp문제도 잘 풀 수 있을것,,! 

# d = [0] * 100 #저장을 위한 dp 테이블 만들기
#
# d[1] = 1
# d[2] = 1
# n = 99
#
#
# #피보나치 함수 반복문으로 구현(보텀업 다이나믹 프로그래밍)
#
# for i in range(3, n+1):
#     d[i] = d[i-1] + d[i-2]
#
# print(d[n])


'''

뒤에서 부터 계산


상담을 하거나, 상담을 안하고 넘기는 경우


dp[i] = max(dp[i]+dp[time[i]+i] , max_pay)
'''


import sys

N = int(input())

timeTable = [list(map(int,sys.stdin.readline().split())) for i in range(N)]

dp = [0 for i in range(N+1)]

for i in range(N-1,-1,-1):
    if i + timeTable[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(timeTable[i][1] + dp[i + timeTable[i][0]], dp[i+1])

print(dp[0])

from sys import stdin

n = int(input())
times = [0]
pays = [0]
for i in range(n):
    t, p = map(int, stdin.readline().split())
    times.append(t)
pays.append(p)

dp = [0] * (n + 2)
max_pay = 0
for i in range(n, 0, -1):
    if i + times[i] > n + 1:
        dp[i] = max_pay
    else:
        if i + times[i] == n + 1:
            dp[i] = max(pays[i], max_pay)
        else:
            dp[i] = max(pays[i] + dp[times[i] + i], max_pay)
    max_pay = max(max_pay, dp[i])

print(max_pay)


#dfs + 백트래킹 방법,, 이런거 어떻게 생각하냐
def revenue_making(idx, rev):
    global max_rev
    if idx == N:
        if max_rev < rev:
            max_rev = rev
        return
    revenue_making(idx+1, rev) #상담을 안 받는 경우
    if idx + table[idx][0] <= N: #상담을 해줄 수 있는 경우
        revenue_making(idx+table[idx][0], rev+table[idx][1])

N = int(input())
table = []
for i in range(N):
    t, p = map(int, input().split())
    table.append((t,p))
max_rev = 0
revenue_making(0, 0)

print(max_rev)