import sys
from collections import deque

input = sys.stdin.readline


def bfs(lst, x,y, nx, ny):
    q = deque([])
    q.append([x,y])
    while q:
        x,y = q.popleft()
        dxl=[-1,-1,1,1,2,2,-2,-2]
        dyl=[2,-2,2, -2, 1, -1, 1, -1]
  
        if x == nx and y == ny:
            print(lst[x][y])
            break
        
        for i in range(8):
            dx = x+dxl[i]
            dy = y+dyl[i]

            if 0<=dx < len(lst) and 0<=dy < len(lst) and lst[dx][dy] == 0:
                lst[dx][dy] = lst[x][y] +1
                q.append([dx,dy])
    
for _ in range(int(input())):
    n = int(input())
    lst=[[0]*n for _ in range(n)]
    
    x,y = map(int, input().split())
    nx,ny = map(int, input().split())
    
    bfs(lst, x,y,nx, ny)
   


      
    
    