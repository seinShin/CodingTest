# 14235 크리스마스 선물
import sys
from queue import PriorityQueue

n = int(input())
gift = PriorityQueue()
for _ in range(n):
    a = list(map(int, input().split()))
    
    if a[0] != 0:
        for i in range(1, len(a)):
            gift.put((-a[i], a[i]))
    else:
        if gift.empty():
            print(-1)
        else:
            print(gift.get()[1])    
        
    