'''


정올 단어집합 2


'''


flag = True
ans = []
while flag:

    words = input().split()

    if words == ["END"]:
        break

    for word in words:
        if word not in ans:
            ans.append(word)
        else:
            pass
    print(*ans)








