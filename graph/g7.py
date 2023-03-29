import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
    
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(graph, a, b):
    q = deque()
    q.append([a,b])
        
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]    
            ny = y+dy[i]
            
            if nx<0 or nx >=n or ny<0 or ny>= m:
                continue
        
            if graph[nx][ny] == 1 and (nx+ny != 0):
                graph[nx][ny] = graph[x][y] +1
                q.append([nx,ny])
            
bfs(graph, 0, 0)

print(graph[n-1][m-1])        