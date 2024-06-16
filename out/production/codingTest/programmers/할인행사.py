# 프로그래머스 lv2_할인 행사

def solution(want, number, discount):
    answer = 0
    dic={}
    
    for i in range(len(want)):
        dic[want[i]] = number[i]
        
    start=0
    end = len(discount)-start
    while end >=10:
        tmp=discount[start:start+10]
        
        sts=True
        for i in range(len(want)):
            if dic[want[i]] > tmp.count(want[i]):
                sts=False
                break
                
        if sts == True:
            answer+=1
            
        start+=1
        end = len(discount)-start
        
    return answer


# 간단한 코드
# Counter 이용
# from collections import Counter
# def solution(want, number, discount):
#     answer = 0
#     dic = {}
#     for i in range(len(want)):
#         dic[want[i]] = number[i]

#     for i in range(len(discount)-9):
#         if dic == Counter(discount[i:i+10]): 
#             answer += 1

#     return answer
