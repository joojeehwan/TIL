def is_possible(ans):
    for x, y, stuff in ans:
        # 설치된것이 기둥인 경우
        if stuff == 0:
            # 바닥 위 / 보의 한쪽 끝 부분 위 / 다른 기둥 위 => 정상
            # in => ans안에 [] 안의 값들이 존재하느냐?!
            if y == 0 or [x - 1, y, 1] in ans or [x, y, 1] in ans or [x, y - 1, 0] in ans:
                continue
            return False
        # 설치된것이 보라면?!
        elif stuff == 1:
            # 한 쪽 끝부분이 기둥 / 혹은 양쪽 끝부분이 다른 보와 동시에 연결 = > 정상
            if [x, y - 1, 0] in ans or [x + 1, y - 1, 0] in ans or ([x - 1, y, 1] in ans and [x + 1, y, 1] in ans):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    # 작업(frame)의 개수는 최대 1,000개
    for frame in build_frame:
        # 하나씩 빼서 사용하기 => 문제의 조건들을
        x, y, stuff, operate = frame

        # 삭제하는 경우
        if operate == 0:
            # 일단 삭제한다.
            answer.remove([x, y, stuff])
            # 가능한 구조물인지 확인하기
            if not is_possible(answer):
                # 삭제가 안되는거면 다시 추가
                answer.append([x, y, stuff])

        # 설치하는 경우
        elif operate == 1:
            # 일단 설치를 하고
            answer.append([x, y, stuff])
            # 가능한 구조물인지 확인하기
            if not is_possible(answer):
                # 가능한 구조물이 아니면 다시 제거
                answer.remove([x, y, stuff])
    return sorted(answer)


# print(solution(5,[[1,0,0,1], [1,1,1,1], [2,1,0,1,], [2,2,1,1], [5,0,0,1], [5,1,0,1], [4,2,1,1], [3,2,1,1]]))


# 다른 풀이,set 사용
def impossible(result):
    COL, ROW = 0, 1
    for x, y, a in result:
        if a == COL:  # 기둥일 때
            if y != 0 and (x, y - 1, COL) not in result and \
                    (x - 1, y, ROW) not in result and (x, y, ROW) not in result:
                return True
        else:  # 보일 때
            if (x, y - 1, COL) not in result and (x + 1, y - 1, COL) not in result and \
                    not ((x - 1, y, ROW) in result and (x + 1, y, ROW) in result):
                return True
    return False


def solution(n, build_frame):
    result = set()

    for x, y, a, build in build_frame:
        item = (x, y, a)
        if build:  # 추가일 때
            result.add(item)
            if impossible(result):
                result.remove(item)
        elif item in result:  # 삭제할 때
            result.remove(item)
            if impossible(result):
                result.add(item)
    answer = map(list, result)

    #람다는 이런식으로,,! 사용!
    return sorted(answer, key=lambda x : (x[0], x[1], x[2]))
    # return sorted(answer, key=lambda x: (x[0], x[1], x[2]))