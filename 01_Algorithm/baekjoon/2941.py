

'''

내장 함수 안쓰고 가능한가,,?

토욜에 고민 좀 해보자,,


replace

'''



target = ["c=",  "c-", "dz=", "d-", "lj", "nj", "s=", "z="] #타켓이 되는 크로아티아 문자

str_lst = input() #기본적인 입력

for i in target:
    str_lst = str_lst.replace(i, "#")
#주어진 크로아티아 문자들을 하나로 세기 위해서 랜덤한 문자 하나로 바꿈! 


print(len(str_lst))




'''

스택으로도 접근이 가능해! 



'''