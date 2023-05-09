import sys
from collections import deque

# 13549 bfs

input = sys.stdin.readline

n,k = map(int, input().split())
lst=[0]*100001

def bfs(n, k):
    q = deque()
    q.append(n)
    lst[n] = 1
    
    while q:
        start = q.popleft()
        
        if start == k:
            return lst[k]
            
        for i in (start*2,start-1,start+1):
            if i >=0 and i <= 100000 and lst[i] == 0:
                if i == start*2:
                    lst[i] = lst[start]
                    q.appendleft(i)
                else:
                    lst[i] = lst[start]+1
                    q.append(i)
                    

print(bfs(n,k)-1)

            