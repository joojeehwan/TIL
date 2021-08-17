"""
1210: ladder1
"""

# import sys
# sys.stdin = open('1210_input.txt')







T = 10

for tc in range(T):

    N = int(input())
    size = 100
    MAP = []

    MAP = [list(map(int, input().split())) for _ in range(size)] #이것이 이차원 배열 받는 거였지,,! 

    visted = [[0] * size for _ in range(size)] 

    row = size - 1
    col = 0
    for i in range(size):
        if MAP[row][i] == 2:
            col = i
    
    #왼오위,,! 배열안 배열 생각하면 쉽다,,! 
    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    while row > 0:
        de = 1
    
        for i in range(3):
            next_row = row + dr[i]
            next_col = col + dc[i]
        
            #이걸로 내려갈 수 있음
            if next_row < 0 or next_col < 0 or \
                next_row >= size or next_col >= size:
                continue
        
            if visted[next_row][next_col] == 1:
                continue

            if MAP[next_row][next_col] == 1:
                row = next_row
                col = next_col
                visted[row][col] = 1
                break
        
    print("#{} {}".format(tc + 1, col))
                

