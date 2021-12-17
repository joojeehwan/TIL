# flag = True
#
#
# while flag :
#
#     #리스트 형식으로 빈 칸 기준 나눠서 입력받기
#     words = list(input().split())
#
#     #만약 END면 그만두기
#
#     if words == ["END"]:
#         flag = False
#         break
#
#
#     else:
#         #갯수를 카운팅할때 기준이 되는 배열이 된다.
#         word_list = []
#         for word in words:
#             word_list.append(word)
#
#         #words의 각 단어를 추가한 word_list를 set화 하면서 중복제거
#         #다시 리스트로 만들고 sort로 정렬
#
#         word_list = set(word_list)
#         word_list = list(word_list)
#         # print(word_list)
#         #문제에서 오름차순 크기로 정렬하라고 말함
#         word_list.sort()
#         # print(word_list)
#
#         word_count = [0] * len(word_list)
#
#         #이중포문으로 두 배열 완전검색 돌림
#         for word in words:
#             for i in range(len(word_list)):
#                 #만약 words의 word와 word_list의 i번째 단어와 같다면
#                 #word_count의 i번쨰에 개수 1 추가
#                 if word == word_list[i]:
#                     word_count[i] += 1
#
#         for i in range(len(word_list)):
#             print(f"{word_list[i]} : {word_count[i]}")

flag = True
while flag:

    words = input().split()
    count_dict = {}

    if words == ["END"]:
        falg = False
        break

    for word in words:
        #만약에 words에 있는 단어가 count_dict의 key에 없으면!?
        if word not in count_dict.keys():
            #새롭게 dict에 추가 하면서 0으로 초기화
            count_dict[word] = 0

        #그게 아니라면 갯수 추가!
        count_dict[word] += 1

    #key-value 다 같이 나오는게 items() 메서드임
    #근데 그 key value 중에서 앞에 있는 key(단어) 기준 오름차순 정렬
    count_items = sorted(count_dict.items(), key=lambda x: x[0])

    for item in count_items:
        print(f"{item[0]} : {item[1]}")







