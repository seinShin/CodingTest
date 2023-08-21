# 2346 풍선 터뜨리기
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
d= deque()
answer=[]

for i in range(n):
    d.append((lst[i], i+1))
    
move, index = d.popleft()
answer.append(index)

for i in range(n-1):
    if move > 0:
        d.rotate(-(move-1))
    else:
        d.rotate(-move)
        
    move, index = d.popleft()
    answer.append(index)

print(*answer)


    

