# 2014 소수의 곱
# import sys, heapq
# from itertools import combinations_with_replacement
# from math import prod

# input = sys.stdin.readline
# k,n = map(int, input().split())
# lst=list(map(int, input().split()))
# q = []
# rst=0
# for i in range(1, k+1):
#     for combi in combinations_with_replacement(lst, i):
#         q.append(prod(list(combi)))

# heapq.heapify(q)

# for _ in range(n):
#     rst = heapq.heappop(q)
    
# print(rst)

## 메모리 초과

import sys, heapq

input = sys.stdin.readline

k,n = map(int, input().split())
lst=list(map(int, input().split()))

heap=[]
visited=set()
max_value=max(lst)

for i in lst:
    heapq.heappush(heap, i)
    
for i in range(n-1):
    ele = heapq.heappop(heap)
    
    for x in lst:
        num = ele*x
        
        if len(heap) >=n and max_value <num:
            continue
        if num not in visited:
            heapq.heappush(heap, num)
            max_value = max(max_value, num)
            visited.add(num)
            
            
print(heapq.heappop(heap))