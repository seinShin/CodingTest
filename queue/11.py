import sys
from collections import deque

input = sys.stdin.readline

n,k = map(int, input().split())

lst=deque([i for i in range(1,n+1)])
rst=[]
for i in range(n):
    for j in range(k-1):
        x = lst.popleft()
        lst.append(x)
    x = lst.popleft()
    rst.append(x)
    
print('<', end='')
for i in range(len(rst)):
    if i<len(rst)-1:
        print(rst[i], end=', ')
    else:
        print(rst[i], end='')
print('>')    


