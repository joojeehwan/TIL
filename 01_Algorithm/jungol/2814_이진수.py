'''


2814 이진수



입력된 2진수를 10진수로 변환하여 출력한다.

'''


N = list(input())


N.reverse()

#answer에 더해나간다.
ans = 0


for i in range(len(N)):
    #만약 i번째 값이 "1"이면
    if N[i] == "1":
        #answer에 2의 i승 만큼 더해줌
        ans += 2**(i)

print(ans)


# def change(lst):
#
#     ans = 0
#     n = len(lst)
#     for i in range(n):
#         ans = ans*2 + (lst[i]-'0')
#
#     return ans
#
#
# print(change(N))









