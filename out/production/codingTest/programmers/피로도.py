
# 프로그래머스 lv2_피로도
# 데이터의 크기가 크지 않아 순열을 써도 효율성에 걸리지 않았지만 dfs를 이용하자

from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    for p in permutations(dungeons, len(dungeons)):
        tmpList=list(p)
        stat=k
        cnt=0
        for i in range(len(tmpList)):
            if tmpList[i][0] <= stat:
                stat-=tmpList[i][1]
                cnt+=1
            else:
                break
        answer = max(answer, cnt)
    return answer