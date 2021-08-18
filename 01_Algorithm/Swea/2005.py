"""
2005: 파스칼의 삼각형
""" 

# import sys
# sys.stdin = open('2005_input.txt')


# #전혀 몰랐음



T = int(input())

N = int(input())


lst = [[0] * i for i in range(1,N+1)]


for i in range(len(lst)):
    for j in range(len(lst[i])):
        if i == j :
            lst[i][j] = 1

        elif j == 0:
            lst[i][j] = 1

        else:
            lst[i][j] = lst[i-1][j-1] + lst[i-1][j]

print(f"#{T}", end="")
for i in range(len(lst)):
    print()
    for j in range(len(lst[i])):
        print(lst[i][j], end=" ")
        


