'''



직사각형 네개의 합집합의 면적 구하기 


좌표가 주어짐!

나 이거 비슷한거 풀어보았다!
그거다! 과목평가 때!

겹치는 것을 두려워 하지마라! 배열에 값을 1을 넣어놓고 전체에서
1인것의 개수를 구하면 되지 않느냐하?!




'''


x1, y1, x2, y2 = map(int, input().split())

x3, y3, x4, y4 = map(int, input().split())

x5, y5, x6, y6 = map(int, input().split())

x7, y7, x8, y8 = map(int, input().split())

MAP = [[0]*100 for _ in range(100)]


for row in range(x1, x2):
    for col in range(y1, y2):
        MAP[row][col] = 1

for row in range(x3, x4):
    for col in range(y3, y4):
        MAP[row][col] = 1

for row in range(x5, x6):
    for col in range(y5, y6):
        MAP[row][col] = 1

for row in range(x7, x8):
    for col in range(y7, y8):
        MAP[row][col] = 1

cnt = 0

for row in range(100):
    for col in range(100):
        if MAP[row][col] == 1:
            cnt += 1

print(cnt)
