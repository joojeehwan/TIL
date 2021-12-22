''''

카드 정렬하기,,!


heapq를 사용하는,,! 좋은 문제
자료구조를 사용해서 알고리즘 문제를 해결하는,,,!

'''





import heapq

n = int(input())

heap = []

for i in range(n):

    data = int(input())
    heapq.heappush(heap, data)


res = 0

while len(heap) != 1:
    #가장 작은 2개의 카드 묶음 꺼내기
    fir = heapq.heappop(heap)
    sec = heapq.heappop(heap)

    #카드 묶음을 다시 묶어서 다시 삽입
    SUM = fir + sec
    #여기서 더하고 온다! 그래서 하나 남을떄까지 하면 알괴즘 끝!
    res += SUM
    heapq.heappush(heap, SUM)

print(res)