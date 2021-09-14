'''

종이 자르기


일단 입력을 받아 볼까?!


이 문제 풀이의 완성은,, 처음에 0을 넣고 정렬 후에 길이를 넣는 다는 것!

why? 길이를 계산해야 하니깐,,!!


가로점을 기준으로

아래에서 부터 밑으로 내려가면서, 점이 나올때마다 배열에 나온 점을 i i-1로 뺴나가면 그것이 바로 길이,,!!

'''


hor, ver = map(int, input().split())

N = int(input())

lst_hor = [0] #포인트
lst_ver = [0]
for _ in range(N):

    type, number = map(int, input().split())

    if type == 0:
        lst_hor.append(number)
    else:
        lst_ver.append(number)


#길이가 어떻게 생기냐면?!

lst_hor_sorted = sorted(lst_hor)
lst_ver_sorted = sorted(lst_ver)

lst_hor_sorted.append(ver) #포인트
lst_ver_sorted.append(hor)


#이중 포문 돌릴 생각 왜 못하니? 개자슥아?!

max_hor = 0
for i in range(1, len(lst_hor_sorted)):
    gap_hor = lst_hor_sorted[i] - lst_hor_sorted[i-1]
    if gap_hor > max_hor:
        max_hor = gap_hor


max_ver = 0
for j in range(1, len(lst_ver_sorted)):
    gap_ver = lst_ver_sorted[j] - lst_ver_sorted[j-1]
    if gap_ver > max_ver:
        max_ver = gap_ver

print(max_hor * max_ver)



