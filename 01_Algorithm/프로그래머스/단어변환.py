#bfs 풀이

from collections import deque


def solution(begin, target, words):
    answer = 0
    # target이 words에 없는 경우 0 리턴
    if target not in words:
        return 0

    q = deque()
    q.append((begin, 0))
    while q:
        now, depth = q.popleft()
        for word in words:
            diff = 0
            for i in range(len(word)):  # 하나 다른 것 찾기! 타겟 글자와 words안의 word가 다른지 본다.
                if now[i] != word[i]:
                    diff += 1
            if (diff == 1) and (word == target):
                depth += 1
                return depth
            elif diff == 1:
                q.append((word, depth + 1))

    return answer
