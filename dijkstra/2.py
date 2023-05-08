import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

N,E = map(int, input().split())

graph=[[] for _ in range(N+1)]


def dijkstra(start):
    dp=[INF]*(N+1)
    dp[start] = 0
    h = []
    heapq.heappush(h, (0, start))
    
    while h:
        wei, now = heapq.heappop(h)
        
        if dp[now] <wei:
            continue
        
        for next, w in graph[now]:
            next_wei = w+ wei
                
            if next_wei < dp[next]:
                dp[next] = next_wei    
                heapq.heappush(h, (next_wei,next))
    return dp


for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
        
v1, v2 = map(int, input().split())

rst= dijkstra(1)
rst2= dijkstra(v1)
rst3= dijkstra(v2)

v1_path = rst[v1] + rst2[v2] + rst3[N]
v2_path = rst[v2] + rst3[v1] + rst2[N]

result = min(v1_path, v2_path) 
print(result if result<INF else -1)


                