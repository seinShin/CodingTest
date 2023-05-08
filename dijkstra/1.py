import heapq
import math

V,E = map(int, input().split())

graph={ i:{} for i in range(1, V+1)}

start = int(input())

for i in range(E):
    u,v,w = map(int, input().split())
    dic = graph[u]
    dic[v]=w
    graph[u] = dic
    

dist={ vt: [float('INF'), start] for vt in graph}
dist[start] = [0,start]
q=[]

heapq.heappush(q, [dist[start][0], start])

while q:
    cur_dist, cur_vt = heapq.heappop(q)
    
    if dist[cur_vt][0] <cur_dist:
        continue
    
    for adj, weight in graph[cur_vt].items():
        new_dist = cur_dist + weight
        if new_dist < dist[adj][0]:
            dist[adj] = [new_dist, adj]
            heapq.heappush(q, [new_dist, adj])
         
for i in range(1,len(dist)+1):
    if math.isinf(dist[i][0]):
        print('INF')    
    else:
        print(dist[i][0])
# import sys
# input = sys.stdin.readline
# INF = sys.maxsize
# V,E = map(int, input().split())
# k = int(input())

# dp = [INF]*(V+1)
# heap = []
# graph=[[] for _ in range(V+1)]

# def dijkstra(start):
#     dp[start] = 0
#     heapq.heappush(heap, (0, start))

#     while heap:
#         wei, now = heapq.heappop(heap)
        
#         if dp[now] <wei:
#             continue
    
#         for w, next_node in graph[now]:
#             next_wei = w+ wei
            
#             if next_wei < dp[next_node]:
#                 dp[next_node] = next_wei
#                 heapq.heappush(heap, (next_wei, next_node))
                
# for _ in range(E):
#     u,v,w = map(int, input().split())
#     graph[u].append((w,v))


# dijkstra(k)

# for i in range(1, V+1):
#     print("INF" if dp[i] == INF else dp[i])

    