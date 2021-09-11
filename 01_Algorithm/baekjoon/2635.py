'''


수 이어가기

구현   / 부르트 포스



가장 양수를 많이 발생시키는 것,, 어떻게 찾을까?!

while문 쓰면서 전부 확인하면서 가는게 좋을거 같은데?!

일단 두번째 수는 무조건 첫번째 주어지는 수보다는 작은 거자나?! 그치?!

첫번쨰 주어진 수보다 작은 것들을 다 돌려보면서 그 중에서 가장 많이 가는 것을 선택하면 될꺼 같음!


'''



def make_lst(start_num, second_num):

    ans = [start_num, second_num]
    i = 0
    while True:
        ans.append(ans[i] - ans[i + 1])
        if ans[i + 2] < 0:
            break
        i += 1
    ans.pop(-1)

    return ans


N = int(input())
res = 0
max_len = 0

for num in range(N+1):

    lst = [N, num]

    i = 0
    while True:
        lst.append(lst[i] - lst[i+1])
        if lst[i+2] < 0:
            break
        i += 1

    if len(lst) > max_len:
        max_len = len(lst)
        res = num

print(max_len - 1)
print(*make_lst(N, res))


