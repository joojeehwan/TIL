





T = int(input())

for tc in range(1, T+1):

    str1 = input()
    
    stack = []
    
    ans = 0

    for i in range(len(str1)):
        now = str1[i]
        
        if now == "(":
            stack.append(i)
        else: #닫는 괄호
            pop = stack[-1]

            stack.pop(-1)

            if pop == i -1 :
                ans += len(stack)

            else:
                ans += 1

    print("#{} {}".format(tc + 1, ans))