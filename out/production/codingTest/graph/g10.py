import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

max = 10**5
rst=[0]*(max+1)

def bfs(x):
    q = deque([])
    q.append(x)
    
    while q:
        x = q.popleft()
        
        if x == k:
            print(rst[k])
            break
            
        for i in (x-1,x+1,x*2):
            
            if i >=0 and i <= max and not rst[i]:
                rst[i] = rst[x] +1
                q.append(i)
bfs(n)   