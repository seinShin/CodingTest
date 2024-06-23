from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
lst = deque(list(map(int, input().split())))
cnt=0

q=deque([])
for i in range(1,n+1):
    q.append(i)
    
while lst:
    x = lst[0]
    if q[0] == x:
        q.popleft()
        lst.popleft()
    else:
        if q.index(x) < len(q)/2:
            while q[0] != x:
                q.rotate(-1)
                cnt+=1
            q.popleft()
            lst.popleft()
        else:
            while q[0] != lst[0]:
                q.rotate(1)
                cnt+=1
            q.popleft()
            lst.popleft()
print(cnt)
                