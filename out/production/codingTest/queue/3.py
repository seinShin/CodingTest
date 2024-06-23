from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
q = deque([])

for i in range(1,n+1):
    q.append(i)

rst=[]
while len(q) != 0:
    q.rotate(-k+1)
    x=q.popleft()
    rst.append(x)
print('<', end='')
print(*rst, sep=', ', end='')
print('>')