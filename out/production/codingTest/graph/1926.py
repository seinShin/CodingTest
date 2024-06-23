# 1926 그림
from collections import deque
import sys
sys.stdin=open("input.txt","r")
input = sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(i,j, paper):
    q = deque()
    q.append((i,j))
    paper[i][j] = 0
    wid=1
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            x2 = x + dx[i]
            y2 = y + dy[i]
            
            if x2<0 or x2>=len(paper) or y2<0 or y2>=len(paper[0]):
                continue
            
            if paper[x2][y2] == 1:
                wid+=1
                paper[x2][y2] = 0
                q.append((x2,y2))           
    return wid
        


n,m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

cnt=0
width=0
for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            cnt+=1
            width=max(width, bfs(i,j,paper))
  
print(cnt)          
print(width)