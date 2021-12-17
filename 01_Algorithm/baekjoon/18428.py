''''

감시 피하기


'''


from itertools import combinations


n = int(input())

#일단 이렇게 공간을 나누는게 제일 중요
MAP = [] #복도 정보
teachers = [] #모든 선생님 위치정보
spaces = [] #모든 빈 공간 위치 정보


for i in range(n):

    MAP.append(list(input().split()))
    for j in range(n):
        #선생님이 존재하는 위치 저장
        if MAP[i][j] == "T":
            teachers.append((i, j))
        if MAP[i][j] == "X":
            spaces.append((i, j))

#특정 방향으로 감시를 진행(학생 발견 True, 미발견 False)

def watch(row, col, dir):

    #while들의 값들은 MAP의 경계값들
    #학생 만남을 위해 조건 주고 
    #장애물을 만남을 아래에 조건을 주면 장애물 만나는 순간
    #학생을 만나지 않는거니깐 바로 return값을 주면되!
    #학생 -> 장애물 if 문 순서에 의미가 있음
    #왼쪽 방향으로 감시

    if dir == 0:
        #반복문 사용해서 가능하다!
        #while문 반복으로 값을 변화시키면서 확인이 가능!
        while col >= 0:
            if MAP[row][col] == "S":
                return True
            
            if MAP[row][col] == "O":
                return False
            col -= 1
    #오른쪽 방향 
    if dir == 1:
        while col < n:
            if MAP[row][col] == "S":
                return True
            
            if MAP[row][col] == "O":
                return False
            
            col += 1

    #위쪽 방향
    if dir == 2:
        while row >= 0:
            if MAP[row][col] == "S":
                return True

            if MAP[row][col] == "O":
                return False

            row -= 1

    #아래쪽 방향
    if dir == 3:
        while row < n:
            if MAP[row][col] == "S":
                return True

            if MAP[row][col] == "O":
                return False

            row += 1
    return False


#장애물 설치 이후에, 한명이라도 학생이 감지 되는지 검사
def process():

    #모든 선생님들의 위치를 하나씩 확인
    for row, col in teachers:
        #4가지 방향으로 학생을 감지 할 수 있는지 확인
        for i in range(4):
            if watch(row, col, i):
                return True
    return False


#학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부
find = False


#빈공간에서 3개를 뽑는 모든 조합을 확인
#아이렇게 하면,,!
for data in combinations(spaces, 3):

    #print(data)
    #빈공간에 설치할 수 있는 경우의 수 만큼 장애물 설치
    for row, col in data:
        MAP[row][col] = "O"

    #학생이 한명도 감지 되지 않는 경우
    if not process():
        #우리가 찾고 있던 것!
        find = True
        break

    #설치 한거 다시 치우기! 다음번 반복을 위해서!
    for row, col in data:
        MAP[row][col] = "X"

if find:
    print("YES")

else:
    print("NO")
