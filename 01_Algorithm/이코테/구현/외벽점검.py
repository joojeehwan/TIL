'''

순열에 대해 복습하고 가자!
나올때마다 다시 복습하자!

순열과 조합에 대해서!

카카오 2020 기출
'''



# input_list = [1,2,3,4,5]
#
# checked = [0] * len(input_list)


# #순열
# def perm(arr, lev):
#     if lev == len(input_list):
#         print(arr)
#         return
#
#     for i in range(len(input_list)):
#         #사용되지 않은 녀석만
#         if not checked[i]:
#             checked[i] = 1
#             arr.append(input_list[i])
#             perm(arr, lev + 1)
#             arr.pop()
#             checked[i] = 0
#
# perm([], 0)



#조합

# nums = [1,2,3,4,5]
#
# ans_list = []
#
# def combi(lev, arr):
#
#     if lev == len(nums):
#         temp = [i for i in arr]
#         ans_list.append(temp)
#         return
#
#     arr.append(nums[lev])
#     combi(lev + 1, arr)
#     arr.pop()
#     combi(lev + 1, arr)
#
#
# combi(0, [])
# print(ans_list)


#nCr

# nums = [1, 2, 3, 4, 5]
# answer_list = []
#
# def nCr(n, ans, r):
#     if n == len(nums):
#         if len(ans) == r:
#             temp = [i for i in ans]
#             answer_list.append(temp)
#         return
#     ans.append(nums[n])
#     nCr(n + 1, ans, r)
#     ans.pop()
#     nCr(n + 1, ans, r)
#
# nCr(0, [], 2)
# print(answer_list)

'''

for 모든 시작점을 

    for 그 시작점에 갈 수 있는 친구들의 경우의 수 순열
    
        for 실제로 친구들이 갈 수 있는 position을 갱신하면서 친구들의 수를 늘려감
        
            if postion이 모든 


'''

from itertools import permutations


def solution(n, weak, dist):
    # 길이를 2배로 늘려서 "원형"을 일자 형태로 변형 => 이게 정말 대단한 생각!

    length = len(weak)
    for i in range(length):
        # weak에서 전체 길이 만큼 +n이 되어야 하는 것처럼!
        weak.append(weak[i] + n)

    print(weak)
    # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    # 왜냐면 친구가 다 들어가야지만 외벽점검을 할 수도 있으니깐!
    answer = len(dist) + 1

    # 0부터 length - 1 까지의 위치를 각각 시작점으로 설정
    # 그치! 2개 배열 이어 붙인거 그 이후가 시작점이 될리는 없지!
    # 원형을 표현하기 위해서 쓴거라서
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인

        # 주의! 리스트에 담아야 한다!
        for friends in list(permutations(dist, len(dist))):
            # print(friends)
            # 투입할 친구의 수
            count = 1
            # 해당 친구가 점검 할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]

            # 시작점부터 모든 취약 지점을 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                #start값이 변함에 따라 index값도 변하고 position의 값도 변해서!
                #아래의if문으로 외벽을 잘 검사하는 지 확인이 가능
                if position < weak[index]:
                    # 새로운 친구를 더 투입
                    count += 1
                    # 더 투입이 불가능하다면 종료
                    if count > len(dist):
                        break
                    #그 다음 친구가 그 취약점부터 자기영역 만큼 확인하려 함,,! 
                    position = weak[index] + friends[count - 1]

            answer = min(answer, count)  # 최솟값 계산
    if answer > len(dist):
        return -1
    return answer







