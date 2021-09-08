'''


뒤집힌 덧셈

형변환


'''



def change_rev(a):

    x = list(map(int, a.rstrip()))

    x_temp = x[::-1]

    x_rev = int("".join(map(str, x_temp)))

    return x_rev


x, y = input().split()

res = change_rev(str(change_rev(x) + change_rev(y)))

print(res)
