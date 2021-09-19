'''


방 배정


1. 남 / 녀 다른방
2. 한 방에는 같은 학년만
3. 한방에 한명도 가능
4. 한 방에 배정할 수 있는 최대 인원수 k

모든 학생을 배정하기 위해 필요한 방의 최소 개수.

성별 s 여학생 0 , 남학생 1
학년 Y

이차원 배열로 하는데! 인덱스 0번을 여학생이라 하고, 1번을 남학생이라 하고 모으면 되긋다!

그거 뭐더라,, 그 배열 하는 거 이용 함! 카운팅 소트 이용!

'''


#이차원 배열로 받아 버리자 입력,,! 그리고 생각! 탐색을 해보자!

# 남자 배열, 여자 배열 따로 받아서 정렬 하는게 낫겟는데?!

#성별, 학년

#그리고 학년 별로 또 배열 하나 만들면 되겟는데?!

N, K = map(int, input().split())

w_lst = []
m_lst = []

room_cnt = 0

for _ in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        w_lst.append(Y)
    else:
        m_lst.append(Y)

sorted_w = sorted(w_lst)
sorted_m = sorted(m_lst)

#큐로 하면 될거 같기도?! 큐의 개념?! 하나씩 뽑아 새로운거면 방 하나 줘 근데 그 방에 같은 학년이어도 K개 이상이면 새로운 방,,!

# 여자부터 방배정 해보자!
res_sorted_w = [0] * 7 #0학년은 사용하지 않아서! 이렇게 하는 것!
res_sorted_m = [0] * 7

for i in range(len(sorted_w)):
    res_sorted_w[sorted_w[i]] += 1

for j in range(len(sorted_m)):
    res_sorted_m[sorted_m[j]] += 1


for i in range(1, len(res_sorted_w)):

    if res_sorted_w[i] == 0:
        continue

    if res_sorted_w[i] <= K :
        room_cnt += 1

    elif res_sorted_w[i] > K:
        room_cnt += ((res_sorted_w[i] // K) + (res_sorted_w[i] % K))

for i in range(1, len(res_sorted_m)):

    if res_sorted_m[i] == 0:
        continue

    elif res_sorted_m[i] <= K :
        room_cnt += 1

    elif res_sorted_m[i] > K :
        room_cnt += ((res_sorted_m[i] // K) + (res_sorted_m[i] % K))

print(room_cnt)



# memory = [0] * 7
# while True:
#
#     if len(sorted_w) == 0:
#         break
#
#     now = sorted_w.pop[0]
#     memory[now] += 1
#
# if memory[now] > K :
#     room_cnt +=







