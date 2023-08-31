# 11403 경로 찾기
from collections import deque
import sys
input = sys.stdin.readline


def bfs(v):
    visited=[ False for i in range(n+1)]            
    q = deque()
    q.append(v)
    
    while q:
        node = q.popleft()
        
        for x in graph[node]:
            if visited[x] == False:
                visited[x] = True
                q.append(x)
      
    for i in range(1, len(visited)):
        if visited[i] == False:
            print(0, end=" ")
        else:
            print(1, end=" ")

n = int(input())
graph=[ [] for _ in range(n+1)]

for i in range(n):
    lst = list(map(int, input().split()))
    
    for j in range(len(lst)):
        if lst[j] == 1:
            graph[i+1].append(j+1)
            
            
for i in range(n):
    bfs(i+1)
    print()

                
        

            

    



    
    
    


    