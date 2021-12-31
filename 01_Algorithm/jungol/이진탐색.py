

## sorted_list : 정렬된 리스트
## target : 특정 정수. 리스트 안에 존재한다면 인덱스 값을, 존재하지 않는다면 -1을 return한다.


def binary_serach(sorted_list, target):

    left = 0
    right = len(sorted_list) - 1


    while(left <= right):
        ##middle은 left 와 right의 중간지점

        middle = (left + right) // 2

        ## target list[middle]보다 작다. right = middle-1
        if target < sorted_list[middle]:
            right = middle - 1
        ## target list[middle]보다 크다. left = middle+1
        elif sorted_list[middle] < target:

            left = middle + 1
        ## target list[middle]과 같다. 인덱스 반환

        else:
            return middle

    ## while문을 빠져나오는 경우 : right < left
    ## 즉, 리스트 안에 target 존재하지 않는다

    return -1