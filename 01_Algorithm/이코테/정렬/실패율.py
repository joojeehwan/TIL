
'''
1.스테이지의 인덱스를 처음부터 끝까지 확인하면서
    해당 스테이지이에 있는 사람의 수를 check
    
2. 실패율 계산 후 정답배열에 튜플로 저장

3. 해당 스테이지에 속한 사람의 수만큼 전체 사람수에서 삭제

4. 정렬 알고리즘를 사용해 값 출력 => 람다 



'''


def solution(N, stages):
    answer = []
    
    
    length = len(stages)
    #스테이지 번호를 1부터 N까지 증가 시키면서
    
    for i in range(1, N + 1):
        #해당 스테이지에 머물고 있는 사람의 수 계산
        count = stages.count(i)
        
        #실패율 계산
        
        if length == 0:
            fail = 0
            
        else:
            fail = count / length
            
        #리스트에 (스테이지번호, 실패요) 원소 삽입
        
        answer.append((i, fail))
        length -= count
        
    #실패율을 기준으로 각 스테이지 내림차순 정렬
    
    answer = sorted(answer, key=lambda x: x[1], reverse = True)
    #answer = sorted(answer, key=lambda x : x[1], revers= True)
    
    #아 튜플의 형태로 값을 넣었음! 그래서,,,! => 
    answer = [i[0] for i in answer]
    
        
    return answer