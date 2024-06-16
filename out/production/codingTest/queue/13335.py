# 13335 트럭
from collections import deque
import sys
input = sys.stdin.readline

n,w,l = map(int, input().split())
truck = deque(list(map(int, input().split())))
lst = deque([0 for _ in range(w)])
time=0

while truck:
    lst.popleft()
    if len(lst) < w:
        if sum(lst) + truck[0] <= l:
            tmp = truck.popleft()
            lst.append(tmp)
        else:
            lst.append(0)
    time += 1
    
print(time+w)

    
    
    