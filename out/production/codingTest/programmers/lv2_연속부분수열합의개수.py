# 프로그래머스 lv2_연속 부분 수열 합의 개수

def solution(elements):
    total=set()
    for i in range(1, len(elements)+1):
        tmp = elements+elements[:i-1]
        
        for j in range(len(tmp)-(i-1)):
            x=sum(tmp[j:j+i])
            total.add(x)
    return len(total)