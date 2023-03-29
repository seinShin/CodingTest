import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

lst=[]
for i in range(n):
    lst.append(list(map(int, input().rstrip())))

dx=[0,0,1,-1]
dy=[1,-1,0,0]    
        
def bfs(lst,a,b):
    q = deque()
    q.append([a,b])
    lst[a][b] == 0
    cnt =1
    
    while q:
        x,y = q.popleft()
        lst[x][y] = 0
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>= len(lst) or ny<0 or ny>=len(lst):
                continue
            
            if lst[nx][ny] == 1:
                lst[nx][ny] = 0
                q.append([nx,ny])
                cnt +=1
    return cnt

rst = []
for i in range(n):
    for j in range(n):
        if lst[i][j] ==1:
            cnt = bfs(lst, i, j)
            rst.append(cnt)
rst.sort()
print(len(rst))
for i in rst:
    print(i) 