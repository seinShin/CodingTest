import sys
import heapq

# 13549 dijkstra
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(n,k):
    dist=[INF]*100001
    q = []
    dist[n] = 0
    heapq.heappush(q, (0,n))
    
    while q:
        weight, curr = heapq.heappop(q)
        
        if curr == k:
            return dist[k]
        if dist[curr] < weight:
            continue
        
        for cost, next in [(0, curr*2), (1, curr+1), (1, curr-1)]:
            next_w = weight + cost
            if 0<= next <= 100000 and next_w < dist[next]:
                dist[next] = next_w
                heapq.heappush(q, (next_w, next))
                        
n,k = map(int, input().split())
print(dijkstra(n,k))