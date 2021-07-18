def fibo(x):

  if x == 1 or x ==2:
    return 1

  return fibo(x-1) + fibo(x-2)





#피보나치 수열 소스코드(재귀적)

#한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화

d = [0] * 100

# 피보나치 함수를 재귀함수로 구현 (탑다운 다이나믹 프로그래밍)

def fibo(x):

    #종료 조건(1 혹은 2일 때 1을 반환)
    if x == 1 or x ==2:
      return 1

    #이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
      return d[x]

    #아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x -1) + fibo(x - 2)
    return d[x]


print(fibo(99))


#호출 되는 함수 확인
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현 (탑다운 다이나믹 프로그래밍)

def fibo(x):

    #종료 조건(1 혹은 2일 때 1을 반환)
    print('f(' + str(x) + ')', end = " ")
    if x == 1 or x ==2:
      return 1

    #이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
      return d[x]

    #아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x -1) + fibo(x - 2)
    return d[x]


print(fibo(6))


#피보나치 수열 소스코드 (반복적)

d = [0] * 100


d[0] * 100
d[1] = 1
d[2] = 1
n = 99

#피보나치 함수 반복문으로 구현
for i in range(3, n + 1):
  d[i] = d[i-1] + d[i-2]


print(d[n])


#실전문제

#정수 x를 입력받기

x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화

d = [0] * 3001


#다이나믹 프로개밍(Dynamic programming) 진행(보텀업)

for i in range(2, x + 1):
  # 현재의 수에서 1을 빼는 경우
  d[i] = d[i - 1] + 1


  # 현재의 수가 2로 나누어 떨어지는 경우
  if i % 2 == 0:
    d[i] = min(d[i], d[i // 2] + 1)

  #현재의 수가 3으로 나누어 떨어지는 경우
  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)

  #현재의 수가 5로 나누어 떨어지는 경우
  if i % 5 == 0:
    d[i] = min(d[i], d[i // 5] + 1)

print(d[x])

#바탐업 방식


#정수 N을 입력받기

n = int(input())

#모든 식량 정보 입력받기
array = list(map(int, input().split()))


# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

#다이나믹 프로그래밍(Dynamic programming) 진행(보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
  d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])

#정수 N을 입력받기

n = int(input())


#앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1001


#다이나믹 프로그래밍(Dinamic Programming) 진행(보텀업)

d[1] = 1
d[2] = 3
for i in range(3, n+1):
  d[i] = (d[i - 1] + d[i-2] * 2) % 796796

#계산된 결과 

print(d[n])
#정수 N을 입력받기

n = int(input())


#앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1001


#다이나믹 프로그래밍(Dinamic Programming) 진행(보텀업)

d[1] = 1
d[2] = 3
for i in range(3, n+1):
  d[i] = (d[i - 1] + d[i-2] * 2) % 796796

#계산된 결과 

print(d[n])



#정수 N,M을 입력받기 

n, m = map(int, input().split())

#N개의 화폐 단위 정보를 입력받기

array = []
for i in range(n):
  array.append(int(input()))


#한 번 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [10001] * (m + 1)


#다이나믹 프로그래밍(dynamic programming)

d[0] = 0
for i in range(n):
  for j in range(array[i], m + 1):
    if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
      d[j] = min(d[j], d[j - array[i] + 1])



#계산된 결과 출력

if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
  print(-1)

else:
  print(d[m])