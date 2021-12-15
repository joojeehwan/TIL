'''


복호화 키가 "eydbkmiqugjxlvtzpnwohracsf" 와 같이 주어진다고 하자,

그러면 이는 다음과 같다 - a 문자는 e, b 문자는 y, ..., z 문자는 f로 바꿔 준다.

암호화 된 문자는 대소문자 혹은 공백이 올 수 있고 대문자는 대문자로
소문자는 소문자로 치환 규칙에 맞게 출력하고,
공백문자는 그대로 출력한다.


어떻게 된거냐면?!

paswword에 있는 문자 하나하나를
그 문자의 원래 알파벳 순서대로 key에서 따라가면 내가 출력해야할 문자가 나옴!

'''

#1. 입력받은 key / password / 순서대로 이루어진 알파벳 문자열 간의 비교를
# 통해서 구하면 될듯,,!

#2. 소문자, 대문자 관련 python 함수 사용하자 / 아스키 코드 변환 함수

'''
isupper() => 대문자인지 확인하는 함수

upper() => 대문자로 변환환

lower() => 소문자로 변환


<문자열을 아스키 코드로 변환>

ord("a") => 97

<아스키코드를 문자열로 변환하는 함수>

chr(65) => A

'''


key = input()
password = input()


#abc ... z 기준이 되는 원래 알파벳 문자열 만들기 => 잊지말자 문자열도 인덱싱이 가능
alpha = ""
for i in range(97, 123):
    alpha += chr(i)

#print(alpha)

ans = ""

for i in range(len(password)):

    #빈칸이면 그냥 빈칸 추가
    if password[i] == " ":
        ans += " "

    else:
    #빈칸이 아니라면 여기서부터는 대문자 소문자 구분 들어가야 함
        if password[i].isupper():
            for j in range(len(alpha)):
                #현재 password 알파벳 값의 소문자가 위에 만들 알파벳과 같은 경우의

                if password[i].lower() == alpha[j]:
                    ans += key[j].upper()


        #소문자라면
        else:
            for k in range(len(alpha)):
                if password[i] == alpha[k]:
                    ans += key[k]

print(ans)