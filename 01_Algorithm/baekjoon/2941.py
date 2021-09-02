

'''

내장 함수 안쓰고 가능한가,,?

토욜에 고민 좀 해보자,,


replace

'''



target = ["c=",  "c-", "dz=", "d-", "lj", "nj", "s=", "z="]



str_lst = "ljes=njak"


cnt = 0

for i in target:
    str_lst = str_lst.replace(i, "#")


print(len(str_lst))

