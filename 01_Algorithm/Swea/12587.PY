"""
12587: 글자수
"""

# import sys
# sys.stdin = open('12587_input.txt')



#ord는 문자의 유니코드 값을 돌려주는 함수이다. 

T = int(input())

for tc in range(1, T+1):

    str1 = input()
    str2 = input()

    counts = [0] * 256

    for ch in str2:
        counts[ord(ch)] += 1

    max_count = -1

    for ch in str1:
        if max_count < counts[ord(ch)]:
            max_count = counts[ord(ch)]

    print(f"#{tc} {max_count}")
