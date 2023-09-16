# 11000 강의실 배정
import sys, heapq
input = sys.stdin.readline

n = int(input())
lec = []
for _ in range(n):
    start, end = map(int, input().split())
    heapq.heappush(lec, (start, end))
    
    
heap=[]
end = heapq.heappop(lec)[1]
heapq.heappush(heap, end)

cnt=1
for i in range(n-1):
    start2, end2 = heapq.heappop(lec)
    end = heapq.heappop(heap)
    
    if start2 < end:
        heapq.heappush(heap, end)
        heapq.heappush(heap, end2)
        cnt+=1
    else:
        heapq.heappush(heap, end2)
        
print(cnt)
