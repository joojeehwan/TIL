#N을 입력받기

n = int(input())

#N개의 정수를 입력받아 리스트에 저장

array = []
for i in range(n):
  array.append(int(input()))

array = sorted(array, reverse = True)

for i in array:
  print(i, end = " ")



#N을 입력받기
n = int(input())


#N명의 학생 정보를 입력받아 리스트에 자장
array = []
for i in range(n):
  input_data = input().split()
  #이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
  array.append((input_data[0], int(input_data[1])))


#키(key)를 용하여, 점수를 기준으로 정렬
array = sorted(array, key = lambda student: student[1])

#정렬이 수행된 결과를 출력
for student in array:
  print(student[0], end = '')


n, k = map(int, input().split()) # N과 K를 입력받기
a = list(map(int, input().split())) #배열 A의 모든  원소를 입력받기
b = list(map(int, input().split())) #배열 B의 모든 원소를 입력받기

a.sort() #배열 A는 오름차순 정렬 수행
b.sort(reverse = True) #배열 B는 내림차순 정렬 수행


for i in range(k):
  #A의 원소가 B의 원소보다 작은 경우
  if a[i] < b[i]:
    # 두 원소를 교체
    a[i], b[i] = b[i], a[i]
  else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
    break   



print(sum(a)) #배열 A의 모든 원소의 합을 출력