from collections import deque

def change(d, c):
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def start():
    direction = 1 
    endTime = 1  
    x,y = 0, 0  
    visited = deque([[x, y]])  # 방문 위치
    arr[x][y] = 2
    while True:
        y, x = y + dy[direction], x + dx[direction]
        if 0 <= y < N and 0 <= x < N and arr[x][y] != 2:
            if not arr[x][y] == 1:  
                tmp_x, tmp_y = visited.popleft()
                arr[tmp_x][tmp_y] = 0 
            arr[x][y] = 2
            visited.append([x, y])
            
            if endTime in times.keys():
                direction = change(direction, times[endTime])
            endTime += 1
        else:  
            return endTime
   
N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1  
    
L = int(input())
times = {}
for i in range(L):
    X, C = input().split()
    times[int(X)] = C
    
print(start())