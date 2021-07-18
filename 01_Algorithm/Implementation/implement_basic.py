#N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

#L, R, U, D에 따른 이동 방향

dx = [0,0,-1,1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']


#이동 계획을 하나씩 확인
for plan in plans:
  #이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]


  if nx < 1 or ny < 1 or nx > n or ny > n :
    continue

  x,y = nx, ny

print(x, y)

h = int(input())


count = 0
for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가 
      if '3' in str(i) + str(j) + str(k):
        count += 1


print(count)



# 현재 나이트 위치 입력받기

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)] 


#8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
  #이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_column = row + step[1]
  #해당 위치로 이동이 가능하다면 카운트 증가
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1



print(result)



#N,M을 공백으로 구분하여 입력받기

n, m = map(int, input().split())

#방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화

d = [[0] * m for _ in range(n)]

#현재 캐릭터의 x좌표, y좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 #현재 좌표 방문 처리

#전체 맵 정보를 입력받기

array = []
for i in range(n):
  array.append(list(map(int,input().split())))



  #북, 동, 남, 서 방향 정의

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    dirction = 3



#시물레이션 시작
count = 1
turn_time = 0
while True:
  #왼쪽으로 회전
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
  if d[nx][ny] == 0 and array[nx][ny] == 0:
     d[nx][ny] = 1
     x = nx
     y = ny
     count += 1
     turn_time = 0
     continue
  #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우 
  else:
      turn_time += 1
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    #뒤로 갈 수 있다면 이동하기
    if array[nx][ny] == 0:
      x = nx
      y = ny
    #뒤가 바다로 막혀있는 경우
    else:
      break
    turn_time = 0



print(count)
