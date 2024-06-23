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
cnt=1
visited=[0]*(n+1)

def bfs(v):
    # visited=[0]*(n+1)
    # need_visit=list()
    
    # need_visit.append(v)
    
    # while need_visit:
    #     global cnt
    #     node = need_visit.pop(0)

    #     if node not in visited:
    #         visited[cnt] = node
    #         cnt+=1
    #         need_visit.extend(graph[node])
    #     else:
    #         continue
    # return visited
            
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
    