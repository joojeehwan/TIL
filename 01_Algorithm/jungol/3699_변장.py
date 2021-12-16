'''

의상의 분류 별로 어떤 가짓수가 나오는지,,!


문제의 예시
headgear => hat, turban, 없음

eyewear => sunglasses , 없음

 3 * 2 = 6 인데
 
 없음의 경우를 하나 빼서 5개! 


 경우의 수 가짓수가 바로 정올이가 밖에 나갈 수 있는 최대 일수



'''


T = int(input())

for tc in range(1, T + 1):

    #의상의 수 N
    N = int(input())

    cloth_dict = {}
    cloth_list = []
    for _ in range(N):
        cloth_name, cloth_sector = input().split()
        #입력받은 (의류, 종류)를 튜플형식으로 list에 추가
        cloth_list.append((cloth_name, cloth_sector))
        
    #의류이름 중복제거 => set으로 중복제거 하고, 다시 list로 형변환!
    #이런식으로도 중복제거 가능 => 자료구조 활용하기!
    cloth_list = set(cloth_list)
    cloth_list = list(cloth_list)

    #딕셔너리를 이용해서 key-value형태로,,!
    for i in range(len(cloth_list)):
        #만약 의류 종류가 cloth_dict에 있으면 + 1
        ''''
        아래와 같은 구조 좋다! 
        딕셔너리에 값이 없으면 있으면으로 전체리스트에서 딕셔너리로 카운팅하는 구조
        없으면 그 값을 그냥 넣고
        값이 존재하면 += 1로 갱신
        '''
        if cloth_list[i][1] in cloth_dict:
            cloth_dict[cloth_list[i][1]] += 1
        else:
            #없음을 기본으로 해야 하니깐! 이렇게 한것!
            cloth_dict[cloth_list[i][1]] = 2

            
    answer = 1
    for count in cloth_dict.values():
        #dict에서 의류종류별로 정리한 갯수를 차례로 곱하면서 답 구하기
        answer *= count
    answer -= 1

    print(answer)
    


