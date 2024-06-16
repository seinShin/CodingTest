import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visited=[-1]*(n+1)
    q=deque()
    q.append((start,0))
    visited[start] = 0
    
    rst=[0,0]
    while q:
        node, cost = q.popleft()
        
        for node_x, cost_x in graph[node]:
            total = cost+cost_x
            if visited[node_x] == -1:
                visited[node_x] = total
                q.append((node_x, total))
                
                if rst[1] < total:
                    rst[0] = node_x
                    rst[1] = total
    return rst
    

n = int(input())

graph=[[] for _ in range(n+1)]

for i in range(n-1):
    a,b,c = map(int, input().split())
    
    graph[a].append((b,c))
    graph[b].append((a,c))
    
s,e = bfs(1)
print(bfs(s)[1])