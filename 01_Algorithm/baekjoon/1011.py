'''


Fly me to the Alpha Centauri

그냥 수학 문제라고 하는데? 뭐지?!



이해가 안되는구만,, 다시 읽어보자!

아 어렵다,, 제곱수에 주목해라아,,!


1 1
1 1 1 1
3 1 1 1
4 1 2 1
5 1 2 1 1
6 1 2 2 1
7 1 2 2 1 1
8 1 2 2 2 1
9 1 2 3 2 1
10 1 2 3 2 1 1
11 1 2 3 2 2 1
12 1 2 3 3 2 1
13 1 2 3 3 2 1 1
14 1 2 3 3 2 2 1
15 1 2 3 3 3 2 1
16 1 2 3 4 3 2 1



제곱수 (1, 4, 8, 16,,)

제곱근 : 제곱하면 a가 되는 수를 a의 제곱근이라고 함.,, 수학 어렵다,,

'''

import math



ans = 0
T = int(input())

for tc in range(1, T+1):

    x, y = map(int, input().split())

    dis = y - x

    #제곱근 구하기
    number = math.floor(math.sqrt(dis))

    number_squ = number ** 2

    if dis == number_squ:
        ans = (number * 2) -1

    if number_squ < dis <= number_squ + number:
        ans = (number * 2)

    if number_squ + number < dis :
        ans = (number * 2) + 1

    if dis <= 3:
        ans = dis

    print(ans)







