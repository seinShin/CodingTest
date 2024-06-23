# 1374 강의실

import sys, heapq
input = sys.stdin.readline


n = int(input())
lectures=[]
for _ in range(n):
    
    num, start, end = map(int, input().split())
    heapq.heappush(lectures, (start, end))


# 첫번째 강의가 끝나는 시간
heap=[]
end = heapq.heappop(lectures)[1]
heapq.heappush(heap,end)

cnt=1
for i in range(n-1):
    start2,end2 = heapq.heappop(lectures)
    end = heapq.heappop(heap)
    
    if start2 < end:
        # 강의 시간이 겹칠 경우
        heapq.heappush(heap, end)
        heapq.heappush(heap, end2)
        cnt+=1
    else:
        # 안겹치면 기존 강의실에 넣어
        heapq.heappush(heap, end2)
        
print(cnt)
    

