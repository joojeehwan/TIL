#기본 입력
height = []
for i in range(9):
    height.append(int(input()))


height.sort()

result = sum(height)

for i in range(9):
    for j in range(i+1, 9):
        if result-height[i]-height[j] == 100:
            for k in range(9):
                if k == i or k == j: #빼서 값이 100이 되는 인덱스를 찾아서 뺴버린다!
                    continue
                else:
                    print(height[k])

