import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
graph=[[] for i in range(v+1)]

for i in range(v):
    line = list(map(int, input().split()))
    root = line[0]
    idx = 1
    while line[idx] != -1:
        node = line[idx]
        cost = line[idx+1]
        graph[root].append((node, cost))
        idx+=2
        
def BFS(start):
    q = deque()
    q.append((start, 0))
    visited = [-1]*(v+1)
    visited[start] = 0
    rst = [0, 0] 
    
    while q:
        now, cost = q.popleft()
        
        for adj_node, adj_cost in graph[now]:
            if visited[adj_node] == -1:
                total = cost + adj_cost
                q.append((adj_node, total))
                visited[adj_node] = total
                if rst[1] < total:
                    rst[0] = adj_node
                    rst[1] = total
        
    return rst

s,e = BFS(1)
print(BFS(s)[1])
                