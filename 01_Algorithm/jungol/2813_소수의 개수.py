'''


2813 소수의 개수

에라토스테네스의 체를 사용해야 함

알고리즘
2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다. 그림에서 회색 사각형으로 두른 수들이 여기에 해당한다.
2는 소수이므로 오른쪽에 2를 쓴다. (빨간색)
자기 자신을 제외한 2의 배수를 모두 지운다.
남아있는 수 가운데 3은 소수이므로 오른쪽에 3을 쓴다. (초록색)
자기 자신을 제외한 3의 배수를 모두 지운다.
남아있는 수 가운데 5는 소수이므로 오른쪽에 5를 쓴다. (파란색)
자기 자신을 제외한 5의 배수를 모두 지운다.
남아있는 수 가운데 7은 소수이므로 오른쪽에 7을 쓴다. (노란색)
자기 자신을 제외한 7의 배수를 모두 지운다.
위의 과정을 반복하면 구하는 구간의 모든 소수가 남는다
'''


import math

M, N = map(int, input().split())

array = [True for _ in range(N + 1)] #처음엔 모든 수가 소수인 것으로 초기화 0과 1 제외
array[0] = False
array[1] = False
#에라토스테네스의 채 알고리즘


for i in range(2, int(math.sqrt(N))+1):
    if array[i] == True: #i가 소수인 경우

    #i를 제외한 i의 모든 배수를 지우기
        for j in range(i*i, N+1, i):
            array[j] = False
        # j = 2
        # while i * j <= N :
        #     array[i*j] = False
        #     j += 1


cnt = 0
for i in range(M, N+1):
    if array[i]:
        cnt += 1

print(cnt)

