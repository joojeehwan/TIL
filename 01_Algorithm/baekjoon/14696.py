'''


딱지놀이


리스트로 입력을 받는게 나을까?! 

리스트로 입력받고, 숫자 체크 하는 방식으로! 

1) 하나라도 높은 수가 있으면 그게 있는 배열이 이김

2) 같은 수의 숫자가 있으면 갯수를 확인! 

...

이렇게 1까지 하다가 1까지 숫자의 개수가 같으면 무승부


맨 앞에 있는 숫자는 어차피 안중여하니깐 일단 입력받고 버리자!



2개의 배열 순서대로 정렬하고! 내림차순으로! 그리고 값을 하나씩 서로 비교하면서 값이 작은 게 나오면 그게 바로 ,,! 뭔지 알지!?
'''


lst1 = [1,2,3,4]

lst2 = [4,3,2,1,0]

for i in range(len(lst2)):
    if lst1[i] < lst2[i] :
        print("test")
        break


# 쉽게 풀 수 있는 방법이 있으면 그 방법으로 풀자! count와 sorted 사용하기!
# a = [2,3,3,2, 4]
#
# print(a.count(3))
#
# print(sorted(a, reverse=True))
#
# T = int(input())
#
#
# for tc in range(1, T+1):
#
#
#     lst1 = list(map(int, input().split()))
#     lst2 = list(map(int, input().split()))
#     lst1.pop(0)
#     lst2.pop(0)
#
#     sorted_A = sorted(lst1, reverse=True)
#     sorted_B = sorted(lst2, reverse=True)
#
#     new_len = min(len(sorted_A), len(sorted_B))
#
#     for i in range(new_len):
#         if sorted_A[i] > sorted_B[i]:
#             print("A")
#             break
#         elif sorted_A[i] < sorted_B[i] :
#             print("B")
#             break
#         else:
#             if i == new_len:
#                 print("D")
#
#             else:
#                 try:
#                     if sorted_A[i+1]:
#                         print("A")
#
#                 except:
#                     print("B")


#이거 좋은 풀이다.,,,!

def cards(card_list):  # Input: Map Object
    cards_count = [0, 0, 0, 0] #개수를 세는 카운트 배열 만들기!
    ls = list(card_list) #맵 오브젝트니깐!
    card_number = ls.pop(0)
    for i in range(card_number):
        cards_count[ls[i] - 1] += 1 #카운트 배열 채우기!
    return cards_count.reverse()  # To prevent reversed-list problem


def shobu(A_cards, B_cards):
    for i in range(4):
        if A_cards[i] > B_cards[i]:  # A win -> return 1
            return 1
        elif A_cards[i] < B_cards[i]:  # B win -> return -1
            return -1
    return 0  # Draw -> return 0


history = []

N = int(input())

for i in range(N):
    A_cards = cards(map(int, input().split()))
    B_cards = cards(map(int, input().split()))
    history.append(shobu(A_cards, B_cards))

for his in history:
    if his == 1:
        print('A')
    elif his == -1:
        print('B')
    else:
        print('D')


# 경기 수 입력
N = int(input())

# 경기 수만큼 반복
for _ in range(N):
    # A의 문양 수, 문양 목록
    A_count, *A_card = map(int, input().split()) # 오 이것도 좋다!
    # B의 문양 수, 문양 목록
    B_count, *B_card = map(int, input().split())

    # 별 > 원 > 사각형 > 삼각형의 수가 많을 수록 이기므로 내림차순 정렬
    A_card = sorted(A_card, reverse=True)
    B_card = sorted(B_card, reverse=True)

    # A의 입장에서 계산
    try:
        # A의 문양 수만큼 반복
        for card in range(A_count):
            # A가 동일한 문양의 수가 더 많은 경우
            if A_card[card] > B_card[card]:
                result = 'A'
                break
            # B가 동일한 문양의 수가 더 많은 경우
            elif A_card[card] < B_card[card]:
                result = 'B'
                break

        # A의 문양 수를 다 돌았는데 승부가 나지 않은 경우
        else:
            # B의 문양이 남았는지 확인
            try:
                B_card[A_count]
                # 문양이 남았다면 B의 승리
                result = 'B'
            # B도 문양이 남지 않은 경우
            except IndexError:
                # 비김
                result = 'D'

    # B의 문양 수까지 A와 같았지만 A는 문양이 더 남은 경우
    except IndexError:
        result = 'A'

    # 결과 출력
    print(result)


    #여기서 배운게 많다,, 다시 풀어보자 