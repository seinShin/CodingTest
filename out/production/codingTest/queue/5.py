import sys
from collections import deque

input = sys.stdin.readline

q = deque([])
for _ in range(int(input())):
    txt = input().strip().split()
    
    
    if txt[0] == "push_back":
        q.append(int(txt[1]))
    elif txt[0] == "push_front":
        q.appendleft(int(txt[1]))
    elif txt[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])        
    elif txt[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])  
    elif txt[0] == "size":
        print(len(q))
    elif txt[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)  
    elif txt[0] == "pop_front":
        if len(q)==0:
            print(-1)
        else:
            x = q.popleft()
            print(x)        
    elif txt[0] == "pop_back":
        if len(q)==0:
            print(-1)
        else:
            x = q.pop()
            print(x)    