'''



1534 10진수를 2,8,16 진수로 변환


'''

# N, B = map(int, input().split())
#
# num_16 = ["A", "B", "C", "D", "E", "F"]
#
# ans = ""
#
# while N > 0:
#
#     #N을 B로 나눈 것의 나머지를 계속 ans에 넣기
#     number = N % B
#
#     #NUM_16의 경우 생각
#     if number >= 10:
#
#         #number는 alpha에 만들어 놓은 문자리스트에서 뽑아가기
#         number = num_16[number-10]
#
#     #진법의 경우 앞에서부터 붙혀줌
#     ans = str(number) + ans
#
#     N = N // B
#
# print(ans)
#
#
# # binary= ""
# # x = 10
# # while x > 0:
# #     div = x // 2
# #     mod = x % 2
# #     x = div
# #     binary += str(mod)
# # binary[::-1]
# #
# # while x > 0:
# #     x, mod = divmod(x,2)
# #     binary += str(mod)
# #
# # binary[::-1]n
# #
# #
# # bin(x)
#
# format(10, "b")


answer = [(1,2),(3,4)]

answer = [i[0] for i in answer]

print(answer)