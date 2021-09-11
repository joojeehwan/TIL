'''

프린터 큐


큐 복습도 하고 좋구만!

bfs 하면서 큐 복습 많이 했음! 악으로 깡으로 버텨라 번개맨 니가 선택한 클럽이다.


이거 임포트 안쓰고 구현을 해봐야 겠는데?! ,,

저정도 모듈은 그냥 해도 되겠다!



문제에선 우선순위가 높은 것을 먼저 뽑으니깐 출력하고 뒤집으면 되지 않을까?!


'''


from queue import PriorityQueue


# que = PriorityQueue()
#
#
# que.put((4, "주지환"))
# que.put((1, "서민정"))
# que.put((7, "주천상"))
# que.put((3, "김미정"))
# que.put((6, "주천상"))
#
# # 튜플로 값을 넣으면! 순번을 정한것에 대한 값을 할 수 있다.
#
# print(que.get()[1])
# print(que.get()[1])
# print(que.get()[1])
# print(que.get()[1])


# from queue import PriorityQueue
#
# q = PriorityQueue()
#
# N = 6 #전체 문자의 갯수
# M = 0 #내가 궁금한 문자의 번호(idx)
#
# lst = [1,1,9,1,1,1] #문자별 idx
#
# for i in range(len(lst)):
#     q.put((lst[i], chr(i+80)))
#
# ans = []
# for _ in range(N):
#     ans.append(q.get()[1])
#
# res = ans[::-1]
#
# for j in range(N):
#     if ans[M] == res[j]:
#         print(j+1)


# 이렇게 풀면은 마지막 테스트 케이스가 설명이 안됌! 그냥 구현으로 ,,!


'''

첫 번째 수가 가장 큰수가 될때까지 앞에서 부터 확인하면서 ,, 
만약에 뒤에 나보다 큰 수가 있으면 뒤로 보내버림! 

그 큰수가 내가 찾는 녀석이면?! 그때의 인덱스를 알려주라! 
만약에 그 녀석이 내가 찾는 녀석이 아니다? 그럼 또 큰녀석 찾고 뒤로 보낸다!

맨 앞에 큰녀석이 되는 순간 프린트 하니깐 큰 녀석을 찾을 떄 순서를 증가시키자!  

근데 이거 인덱스 바뀌는거 기록해야한다! like visted 배열처럼! 
원래 문서의 인덱스를 저장해놓고, 변할때 마다 같이 변하는?! 

와일문 쓰면 좋겠는디?!



이거 하고 런닝가야지,, 뛰고싶다.

아 값이 변하는 것을 방지하자!! 

아 팝하고 append하면 값이 자꾸 바뀐다!! 으으 

와 머리 아프다,,, 으응,, 진짜로

'''
# ans = [1,2,3,4]
# for _ in range(3):
#
#     print(ans)
#
#
#     ans.append(6)







T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())

    order = list(map(int,input().split()))

    first_idx = [x for x in range(len(order))]  #기억할 배열을 만들어 놓는다 약간 비짓배열 만들듯이!
            # 이걸 쓰는게 포인트! 변하는 것을 감지!! 근데 idx쓰면 되지 않았을까?! 흠흠

    ans = first_idx[M] #이거 딥카피 그거인가?! 아닌데,, 리스트 복사하는 것도 아니고!
        # print(first_idx)

    cnt = 0

    while True:

        if order[0] == max(order): # 첫번째 값이 가장 큰값이니?!
            cnt += 1

            if first_idx[0] == ans: #
                print(cnt)
                break
                     #여기서 부터는 그냥 팝해서 버린다! 어차피 if 문 안으로 들어올때 맨앞자리가 큰거는 확인!
            else:
                order.pop(0)
                first_idx.pop(0)
        else:
            order.append(order.pop(0))
            first_idx.append(first_idx.pop(0))















