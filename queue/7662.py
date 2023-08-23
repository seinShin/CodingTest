# 7662 이중 우선순위 큐
import heapq
import sys

input = sys.stdin.readline
q = []

def pop(heap):
    while len(heap)>0:
        data, id = heapq.heappop(heap)
        if not deleted[id]:
            deleted[id] = True
            return data
    return None

for _ in range(int(input())):
    
    k = int(input())
    min_heap=[]
    max_heap=[]
    current = 0
    deleted=[False] *(k+1)
    
    for _ in range(k):
        x, num = map(str, input().split())
        
        if x == "I":
            heapq.heappush(min_heap, (int(num), current))
            heapq.heappush(max_heap, (-1*int(num), current))
            current+=1
        else:
            if int(num) == -1: pop(min_heap)
            elif int(num) == 1: pop(max_heap)
        
    
    max_value = pop(max_heap)
    if max_value == None:
        print("EMPTY")
    else:
        heapq.heappush(min_heap, (-max_value, current))
        print(-max_value, pop(min_heap))