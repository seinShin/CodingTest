import heapq
import sys
input = sys.stdin.readline


lst=[]
for _ in range(int(input())):
    x = int(input())
    
    if x != 0:
        heapq.heappush(lst, (abs(x), x))
    else:
        if len(lst) == 0:
            print(0)
        else:
            y = heapq.heappop(lst)[1]
            print(y)