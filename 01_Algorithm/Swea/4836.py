"""
4836: 색칠하기
"""

import sys

sys.stdin = open('4836_input.txt')


def count_p(grid, color_list):

    for color in color_list:
        horizontal = color[2] - color[0] + 1
        vertical = color[3] - color[1] + 1


        x, y = color[0], color[1]

        for v in range(vertical):
            for h in range(horizontal):
                grid[x + h][y + v] += color[4]

    count = 0
    for i in range(10):
        count += grid[i].count(3)
    return count


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    my_grid =[[0] * 10 for _ in range(10)]
   
    my_color = []
    for n in range(N):
        my_color.append(list(map(int, input().split())))

    print(f"#{tc} {count_p(my_grid, my_color)}")


