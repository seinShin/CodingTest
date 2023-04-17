import heapq
import sys
input = sys.stdin.readline

lst=[]
for _ in range(int(input())):
    x = int(input())
    
    if x != 0:
        heapq.heappush(lst, -x)
    else:
        if len(lst) == 0:
            print(0)
        else:
            y = heapq.heappop(lst)
            print(-y)