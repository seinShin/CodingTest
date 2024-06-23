from collections import deque
import sys 
input = sys.stdin.readline
n = int(input())

q = deque([])
for i in range(n):
    t = input().strip().split()
    
    if t[0] == 'push':
        q.append(t[1])
    elif t[0] == 'front':
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    elif t[0] == 'back':
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])
    elif t[0] == 'size':
        print(len(q))
    elif t[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif t[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            x = q.popleft()
            print(x)
        
    
    
        