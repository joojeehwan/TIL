'''

이전에 교수님과 풀었던 오목 문제 확인해보자!


'''


def check(row, col, color):
    
    global answer
    
    #우향, 우하향, 우상향, 하향만 오목인지 확인하면 됨

    dr = [0, 1, -1, 1]
    dc = [1, 1, 1 , 0]


    for i in range(4):
        over_check_row = row - dr[i]
        over_check_col = col - dc[i]
        #장외를 막는,,!
        if 0 <= over_check_row < 19 and 0 <= over_check_col < 19 and MAP[over_check_row][over_check_col] != color or (over_check_row == -1 or over_check_col == -1) :
            next_row = row + dr[i]
            next_col = col + dc[i]

            count = 1
            while 0 <= next_row < 19 and 0 <= next_col < 19 and MAP[next_row][next_col] == color :
                count += 1
                next_row = next_row + dr[i]
                next_col = next_col + dc[i]

            if count == 5:
                answer = color
                return


MAP = [list(map(int, input().split())) for _ in range(19)]

flag = False

for row in range(len(MAP)):
    for col in range(len(MAP)):
        answer = 0
        if MAP[row][col] == 1 or MAP[row][col] == 2:
            check(row, col, MAP[row][col])

        if answer != 0 :
            flag = True
            print(answer)
            print(row + 1, col + 1)
            break
    if flag == True:
        break

if flag == False:
    print(0)