


T = int(input())

for tc in range(1, T+1):
    str1, str2 = input().split()


    i = 0
    ans = 0
    while i < len(str1) - len(str2) + 1:
        cnt = 0
        for j in range(len(str2)):
            if str1[i + j] == str2[j]:
                cnt += 1

        if cnt == len(str2):
            i += len(str2)

        else:
            i += 1

        ans += 1


    ans += len(str1) - i