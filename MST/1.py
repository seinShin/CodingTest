import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input())) for _ in range(n)]

def bfs(lst, i, j):
    q = deque()
    q.append([i,j])
    lst[i][j] = 0
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    
    cnt=1

    while q:
        x,y = q.popleft()
        lst[x][y] = 0

        for i in range(4):
            newx= x+ dx[i]
            newy = y+dy[i]

            if newx <0 or newx>=n or newy<0 or newy>=n:
                continue
            
            if lst[newx][newy] == 1:
                q.append([newx,newy])
                lst[newx][newy] = 0
                cnt+=1
    return cnt         

rst=[]
for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            cnt = bfs(lst, i, j)
            rst.append(cnt)

print(len(rst))
for i in rst:
    print(i)