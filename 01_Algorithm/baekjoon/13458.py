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








