
'''

그리디 적인 생각을 가져가보자,,! 현재로서 가장 최선의 선택을 계속 하자!

총감독이 무조건 있어야 하나? 꼭 있어야 하나 보다,,! 문제 출력 보니깐 !

=> 그거 아닌거 같은디.,

=> 총감독이 있게된다면 1명만 있으면 되는 것!

최소의 감독 수 니깐!


총감독이 만약에 부 감독의 감시 영역 보다 크다면

총감독 하나씩 넣으면 되고

총감독이 감시하는 영역이 부감독의 감시 영역 보다

 같거나 작다면, 굳이 총감독을 시험에 안넣어도 된다!

근데 값을 빼게 될때! 0이하가 되면 그 다음엔 안 빼도 된다!


1) b와 c를 비교 => b가 큰경우, c가 큰 경우를 나눈다!

아 총감독이 꼭 있어야 하는 거면 저 경우로 나누는게 아니라!!

=> 총감독의 수로 뻇을때 0이 되면 그만하는,,! 그런 식을 만들어야 해!


2) 입력 받은 배열에서 각각의 값에서 b를 뺀다

2-1) 값을 다 한번씩 b만큼 뺴고(뺄 때마다 cnt를 증가) 났을때, 값이 모두 0이하 이면 끝!

3) b를 빼고 나서도 양수인 배열이 존재하면, 그 부분이 0이하가 될때까지 이제는 c를 뺸다

3-1) 값이 있는 것들에서  c를 각각 빼고(cnt증가) 배열이 모두 0이하 가 되면 끝!


'''



import sys

def check_cnt(student):

    flag = 0
    for stu in student:
        if stu <= 0:
            flag += 1

    if flag == len(student):
        return True

    return False



N = int(sys.stdin.readline())

student = list(map(int, sys.stdin.readline().split()))

B, C = map(int, sys.stdin.readline().split())

cnt = 0

for i in range(len(student)):
    student[i] -= B
    cnt += 1

if check_cnt(student):
    print(cnt)

else:
    while sum(student) >= 0:

        for i in range(len(student)):
            if student[i] > 0:
                student[i] -= C #야,, 뭐하니??? 값을 뺀 값을 다시 넣어야지,,!
                cnt += 1

    print(cnt)






#세일 -> 정수단위 올림 ,,,  셀링! 






