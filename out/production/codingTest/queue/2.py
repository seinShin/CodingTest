from collections import deque

q = deque([])

for i in range(int(input())):
    q.append(i+1)

while len(q) >1:
    
    q.popleft()
    
    x = q.popleft()
    q.append(x)
print(q[0])