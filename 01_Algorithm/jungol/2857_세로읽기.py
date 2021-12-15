'''

일단 그냥 입력받아서 세로로 출력하는거만 생각해보자.


'''


# word = [0] * 5
#
# max_len = 0
#
# for i in range(5):
#     #list(input()) 문자열로 들어오는 것을 문자 하나하나 나누어서 담는!
#     word[i] = list(input())
#
#     #이걸 왜 찾냐면! 최대 길이를 알아야
#     #가로 인덱스 시작번호 보다 작은 길이의 가로 문자들은
#     #제끼고 출력을 할 수 있게된다!
#     max_len = max(max_len, len(word[i]))
#
#
# for i in range(max_len):
#     for j in range(5):
#         #여기에 있는 if문이 이 문제의 point
#         #i 값은 오른쪽으로 가는 찍는 인덱스이고 너 몇번쨰 세로 인데?!
#         #j의 값은 아래로 내려가면서 word에 들어가 있는 각각의 문자의 길이를 반환
#         #그래서 i하나씩 찍고 반복하면서 문자가 있는지 없는지 확인 하는 것!
#         if len(word[j]) > i :
#             print(word[j][i], end="")

#다른 풀이



word_list = []

max_len = 0

for _ in range(5):

    input_list = list(input())
    word_list.append(input_list)
    if max_len < len(input_list):
        max_len = len(input_list)


for i in range(5):
    #문자열 중 가장 긴 길이에서 각 문자열들의 길이를 뺴고
    count = max_len - len(word_list[i])

    #만약 그 길이가 0보다 크면 현재 문자열이 짧다는 뜻이므로,,,
    if count > 0:
        #와일 반복문!
        while count > 0:
            # 그 카운트의 만큼 뒤에 ""빈 값 추가
            word_list[i].append("")
            count -= 1

ans = ""


#for문을 세로로 돌리면서

for i in range(max_len):
    for j in range(5):
        # 빈값이면 패스
        if word_list[j][i] == "":
            pass
        else:
            ans += str(word_list[j][i])

print(ans)