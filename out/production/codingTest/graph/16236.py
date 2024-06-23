# 16236 - 아기상어
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
lst = [ list(map(int, input().split())) for _ in range(n)]

x,y, shark = 0,0,2

dx=[0,0,1,-1]
dy=[1,-1,0,0]

## 상어의 위치
for i in range(n):
    for j in range(n):
        if lst[i][j] == 9:
            x,y = i,j
            
## 물고기 잡으러
def bfs(x,y,shark):
    dist = [[0] * n for _ in range(n)]
    visit = [[0] * n for _ in range(n)]

    q = deque()
    q.append((x,y))
    visit[x][y] = 1
    tmp = []
    
    while q:
        cur_x, cur_y = q.popleft()
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0<= nx < n and 0<= ny < n and visit[nx][ny] == 0:
                ## 지나갈 수 있는 부분 확인 후 거리 증가
                if lst[nx][ny] <= shark:
                    q.append((nx,ny))
                    visit[nx][ny]= 1
                    dist[nx][ny] = dist[cur_x][cur_y] +1 
                    
                    ## 먹을 수 있는 상어 체크
                    if lst[nx][ny] < shark and lst[nx][ny] !=0:
                        tmp.append((nx,ny,dist[nx][ny]))
                        
    # 거리순 - 가장 위에 - 가장 왼쪽
    return sorted(tmp, key=lambda x : (-x[2], -x[0], -x[1]))


totalCnt = 0
rst=0

while True:
    
    fishList=bfs(x,y,shark)
    
    ## 엄마 부르기
    if len(fishList) ==0:
        break
    
    nx,ny,dist = fishList.pop()
    
    ## 거리 값이 시간
    rst+= dist
    
    lst[x][y], lst[nx][ny] = 0,0
    x,y = nx, ny
    
    ## 먹은 물고기 수와 상어의 크기가 같다면 상어 크기 증가
    totalCnt += 1
    if totalCnt == shark:
        shark += 1
        totalCnt=0
        
print(rst)
    
