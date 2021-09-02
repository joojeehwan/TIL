'''


2차원 배열이고,,! 좌표가 주어졋네,,!

중복도 어차피 그냥 다 1이라고 해서 넣ㅎ으면,,,!

없는 곳의 영역을 0이라 하고 색칠이 한번이라도 칠해진 곳을 1로 넣어버리고

그곳의 영역의 넓이만 찾으면 되니깐!


'''



N = int(input())


MAP = list([0] * 101 for _ in range(101))

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            MAP[i][j] = 1

answer = 0
for row in MAP:
    answer += row.count(1)

print(answer)