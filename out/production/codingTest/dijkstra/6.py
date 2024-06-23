import sys
import math
import heapq
INF = int(1e9)
input= sys.stdin.readline

# 벨만포드 알고리즘 

def bf(start):
    dist[start] = 0
    
    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next = edges[j][1]
            cost = edges[j][2]
            
            if dist[cur] != INF and dist[next] > dist[cur]+cost:
                dist[next] = dist[cur] +cost
                if i == n-1:
                    return True
    return False



n,m = map(int, input().split())
dist=[INF]*(n+1)
edges=[]
for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((a,b,c))
    
cycle = bf(1)

if cycle:
    print(-1)
else:
    for i in range(2,n+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
        