import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
k= int(input())

graph=[[] for _ in range(n+1)]

for _ in range(k):
    u,v = map(int, input().split())
    
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(n+1):
    graph[i].sort()
    
cnt=0
visited=[0]*(n+1)

def bfs(v):
    global cnt
    
    q = deque([v])
    visited[v] = 1
    
    while q:
        v = q.popleft()
    
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                cnt+=1
bfs(1)      
print(cnt)
                