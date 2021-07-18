n = 2360

count = 0


#큰 단위의 화폐부터 차례대로 확인.
coin_types = [500, 100, 50, 10]



# // : 나누기 연산후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함

for coin in coin_types:
  count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
  n %= coin


print(count)




# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int,input().split())

#N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))


data.sort()    #인덱스 번호가 큰게 큰 값이 정렬되는구나 입력받은 수들 정렬하기
first = data[n-1]
second = data[n-2]

result = 0

while True:
  for i in range(k): #가장 큰수를 k번 더하기
    if m == 0: # m이 0이라면 반복문 탈출
      break
    result += first
    m -= 1 # 더할 때마다 1씩 빼기 
  if m == 0 :
    break
  result += second # 두 번째로 큰 수를 한 번 더하기
  m -= 1
  
print(result)


n, m  = map(int, input().split())

result = 0
for i in range(n): 
  data = list(map(int, input().split()))
  #현재 줄에서 '가장 작은 수' 찾기
  min_value = min(data)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result)


n, k = map(int, input().split())
result = 0

#n이 k 이상이라면 k로 계속 나누기

while n >= k :
  #n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
  while n % k !=0 :
    n -= 1
    result += 1
  n //= k
  result += 1

#마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
  n -= 1
  result += 1



print(result)



