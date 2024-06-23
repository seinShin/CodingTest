# 4963 섬의 개수

import sys
from collections import deque
input = sys.stdin.readline

dx=[0,0,1,-1, 1, -1, 1, -1]
dy=[1,-1,0,0, -1, 1, 1, -1]

def bfs(i, j, h, w):
    q = deque()
    q.append((i, j))
    graph[i][j] = 0
    
    while q:
        next_h, next_w = q.popleft()
        
        for n in range(8):
            x2= next_h+dx[n]
            y2 =next_w+dy[n]

            if x2 <0 or x2 >= h or y2 <0 or y2 >=w:
                continue
            if graph[x2][y2] == 1:
                graph[x2][y2] = 0
                q.append((x2, y2))
   
    return 1

while True:
    w, h = map(int, input().split())
    
    if w == h == 0:
        break
    
    graph=[[] for _ in range(h)]
    
    for i in range(h):
        arr = list(map(int, input().split()))
        graph[i].extend(arr)
    
    cnt=0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                cnt+=bfs(i, j, h, w)
    print(cnt)