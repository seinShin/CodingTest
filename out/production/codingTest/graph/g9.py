import sys
from collections import deque
input = sys.stdin.readline

test=int(input())
dx=[0,0,1,-1]
dy=[1,-1,0,0]


def bfs(lst,a,b):
    
    q = deque()
    q.append([a,b])
    lst[a][b] = 0
    
    while q:
        x,y = q.popleft()
        lst[x][y] = 0
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>= n or ny<0 or ny>=m:
                continue
            
            if lst[nx][ny] == 1:
                lst[nx][ny] = 0
                q.append([nx,ny])
                
for i in range(test):
    cnt=0
    n,m,k = map(int, input().split())
    lst=[[0]*m for _ in range(n)]

    for _ in range(k):
        x,y = map(int, input().split())
        lst[x][y] = 1
    
    for i in range(n):
        for j in range(m):
            if lst[i][j] ==1:
                bfs(lst, i, j)
                cnt+=1
    print(cnt)