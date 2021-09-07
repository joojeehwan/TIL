'''



빙고

내가 알고 있는 빙고룰과 같네! 구현만 잘하면 될것 같다!

숫자가 있는 곳을 체크,,!

빙고를 체크하는 함수를 만들면 좋겠구만,,! 체크하는 번호판을 다 0으로 만들고 숫자가 불리우면 1로 바꾼다!

체크하고 확인하고,, 근데 그게 3빙고 되면 끝!

체크를 어떻게 하냐면 가로, 세로 대각선 보고 합이 5가 되면 1빙고라고 생각하면 된다!




'''


#배운 것 1
# arr=[[1,2], [2,3]]
#
# def sum_arr(arr_2):
#
#     return arr_2[0][0] + arr_2[1][0]
#
# print(sum_arr(arr))

#이차원 배열 그냥 넣어도 된다! 파이썬 만세!


#배운 것 2
# ans = 0
#
# for i in range(5):
#
#     if i == 3:
#         ans = i
#         break
#     print(i)
#
# print(ans)

#배운것 3

'''
result와 bingo_cnt의 위치!

result는 전체 숫자를 넣으면서 break문으로 나갔을 때 확인하는거라,,


bingo_cnt는 숫자 하나 부를 때마다 확인해야 하니깐!! 

'''


size = 5



MAP = [list(map(int, input().split())) for _ in range(size)]

num_2nd = [list(map(int, input().split())) for _ in range(size)]

checked_bingopan = [[0] * size for _ in range(size)]

numbers = []

for i in range(size):
    numbers.extend(num_2nd[i])

# print(MAP)
# print(numbers)
#빙고만 체크하는 함수
    #가로 검사




def check_bingo_ver(arr_2nd):

    check = 0
    for k in range(size):
        sum_ver = 0
        for m in range(size):
            sum_ver += arr_2nd[k][m]

        if sum_ver == size:
            check += 1

    return check

def check_bingo_hor(arr_2nd):
    check = 0
    for k in range(size):
        sum_hor = 0
        for m in range(size):
            sum_hor += arr_2nd[m][k]

        if sum_hor == size:
            check += 1
    return check

def check_bingo_dia_up(arr_2nd):

    check = 0
    sum_dia = 0
    for k in range(size):
        sum_dia += arr_2nd[k][size-1-k]

    if sum_dia == size:
        check += 1
    return check

def check_bingo_dia_down(arr_2nd):

    check = 0
    sum_dia = 0
    for k in range(size):
        sum_dia += arr_2nd[k][k]
    if sum_dia == size:
        check += 1
    return check


result = 0

for i in range(len(numbers)): #사회자가 숫자 하나 부른다
    bingo_cnt = 0

    for row in range(size):
        for col in range(size):
            if MAP[row][col] == numbers[i]:
                checked_bingopan[row][col] = 1
                break


    if check_bingo_ver(checked_bingopan) + check_bingo_hor(checked_bingopan) + check_bingo_dia_up(checked_bingopan) + check_bingo_dia_down(checked_bingopan) >= 3:
        result = i + 1
        break


print(result)



