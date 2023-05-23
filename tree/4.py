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
    res = [0, 0] # start로부터 가장 먼 거리에 있는 노드와 거리 값
    
    while q:
        cnt_node, cnt_dist = q.popleft()
        
        for adj_node, adj_dist in graph[cnt_node]:
            if visited[adj_node] == -1:
                cal_dist = cnt_dist + adj_dist
                q.append((adj_node, cal_dist))
                visited[adj_node] = cal_dist
                if res[1] < cal_dist:
                    res[0] = adj_node
                    res[1] = cal_dist
        
    return res

s,e = BFS(1)
print(BFS(s)[1])
                