import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n,m,v = map(int, input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    u,k = map(int, input().split())
    graph[u].append(k)
    graph[k].append(u)

# bfs
def bfs(v):   
    for i in range(n+1):
        graph[i].sort()
        
    visited=list()
    q = deque([v])
    visited.append(v)
    
    while q:
        v = q.popleft()
        
        for i in graph[v]:
            if i not in visited:
                q.append(i)
                visited.append(i)
    return visited

# dfs
def dfs(v):
    visited=list()
    need_visit=list()
    
    need_visit.append(v)
    while need_visit:
        start = need_visit.pop()
        if start not in visited:
           visited.append(start)
           graph[start].sort(reverse=True)
           need_visit.extend(graph[start])
    return visited
                
    
rst=dfs(v)
print(*rst)


rst2=bfs(v)
print(*rst2) 
                