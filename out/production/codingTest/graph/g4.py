import sys
from collections import deque
sys.setrecursionlimit(10**6)
n,m,r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(n+1):
    graph[i].sort()
    graph[i].reverse()
cnt=1
visited=[0]*(n+1)

def bfs(v):
    global cnt
    
    q = deque([v])
    visited[v] =1
    cnt +=1
    
    while q:
        v = q.popleft()
        
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = cnt
                cnt+=1
            
bfs(r)

print(*visited[1:], sep="\n")
    