"""
1213: String
"""

import sys
sys.stdin = open('1213_input.txt', encoding="UTF8")



T = 10

for tc in range(1, T + 1):

    N = input()
    pattern = input().rstrip()
    text = input().rstrip()


    M = len(pattern)
    N = len(text)


    search_word_count = 0
    i = 0
    j = 0

    while j < M and i < N:
        if text[i] != pattern[j]:
            i = i - j
            j = -1 # 요롷ㄱ
        i = i + 1
        
        j = j + 1
        if j == M:
            search_word_count += 1
            j = -1
        
    print(f'#{tc} {search_word_count}')


