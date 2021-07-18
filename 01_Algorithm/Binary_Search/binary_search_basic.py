#순차 탐색 소스코드 구현

def sequential_search(n, target, array):
  # 각 원소를 하나씩 확인하며
  for i in range(n):
    # 현재의 원소가 찾고자 하는 원소와 동일한 경우
    if array[i] == target:
      return i + 1 #현재의 위치를 반환(인덱스는 0부터 시작하므로 1 더하기)


print("생성할 원소 개수를 입력한 다음 한 칸 뛰고 찾을 문자열을 입력하세요")
input_data = input().split()

n = int(input_data[0]) #원소의 개수
target = input_data[1] #찾고자 하는 문자열을

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()



#순차 탐색 수행 결과 출력

print(sequential_search(n, target, array))


#이진 탐색 소스코드 구현(재귀 함수)

def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  # 찾은 경우 중간점 인덱스 반환

  if array[mid] == target:
    return mid

  #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)

  else :
    return binary_search(array, target, mid+1, end)

#n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))

#전체 원소 입력받기
array = list(map(int, input().split()))

#이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
  print("원소가 존재하지 않습니다.")

else:
  print(result + 1)


# 이진 탐색 소스코드 구현(반복문)

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
      return mid
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
      end = mid - 1
    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
      star = mid + 1
  return None


#n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))


#전체 원소 입력받기
array = list(map(int, input().split()))

  #이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
  print("원소가 존재하지 않습니다.")

else:
  print(result + 1)


import sys

input_data = sys.stdin.readline().rstrip()




#이진 탐색 답안

#이진 탐색 소스코드 구현(반목문)

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
      return mid
  
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인

    elif array[mid] > target:
      end = mid - 1

    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
      start = mid + 1

  return None



#N(가게의 부품 개수) 입력
n = int(input())

#가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))

array.sort() # 이진 탐색을 하기 위해 사전에 정렬 수행

#M(손님이 확인 요청한 부품 개수) 입력

m = int(input())
#손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력

x = list(map(int, input().split()))


#손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
  #해당 부품이 존재하는지 확인
  result = binary_search(array, i, 0, n - 1)
  if result != None:
    print("yes", end = " ")

  else:
    print("no", end = " ")


#계수 정렬 풀이

# N(가게의 부품 개수)을 입력받기
n = int(input()) #기능적으로는 없어도 됨
array = [0] * 1000001

#가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
  array[int(i)] = 1


#M(손님이 확인 요청한 부품 개수 )을 입력받기
m = int(input()) #기능적으로는 없어도 됨
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

#손님이 확인 요청한 부품 번호를 하나씩 확인


for i in x :
  #해당 부품이 존재 하는지 확인
  if array[i] == 1:
    print("yes", end =" ")

  else:
    print("no", end = " ")

#집합 자료형 이용

#N(가게의 부품 개수)을 입력받기

n = int(input)

#가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록

array = set(map(int , input().split()))

#M(손님이 확인 요청한 부품 개수)을 입력받기

m = int(input())

#손님이 확인 요청한 부품 번호를 공백으로 구분하여 입력

x = list(map(int, input().split()))


#손님이 확인 요청한 부품 번호를 하나씩 확인

for i in x:
  if i in array:
    print("yes", end = " ")

  else:
    print("yes", end = " ")





#떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기


n, m = list(map(int, input().split(' ')))

#각 떡의 개별 높이 정보를 입력받기

array = list(map(int, input().split()))


# 이진 탐색을 위한 시작점과 끝점 설정

start = 0
end = max(array)

# 이진 탐색 수행

result = 0
while (start <= end):
  total = 0
  mid = (start + end) // 2

  for x in array:
    #잘렸을 때의 떡의 양 계산





    if x > mid:
      total += x - mid
  # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)

  if total < m:
    end = mid - 1

  # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)

  else:
    result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 resulut를 기록
    start = mid + 1



print(result)