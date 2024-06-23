import sys
import heapq
input = sys.stdin.readline
INF= int(1e9)
# 미확인 도착지
def solution(s,graph):
    dist=[INF] * (n+1)
    dist[s] = 0
    q=[]
    heapq.heappush(q, (0,s))
    
    while q:
        wei, next = heapq.heappop(q)
        
        if dist[next] <wei:
            continue
        
        for next_wei, next_cur in graph[next]:
            wei2 = wei+next_wei
            
            if dist[next_cur] > wei2:
                dist[next_cur] = wei2
                heapq.heappush(q, (wei2, next_cur))
    return dist
    

for i in range(int(input())):
    n,m,t = map(int, input().split())
    s,g,h = map(int, input().split())
    
    graph=[[] for _ in range(n+1)]
    
    for i in range(m):
        a,b,d = map(int, input().split())
        graph[a].append((d,b))
        graph[b].append((d,a))
    
    dtnList = []
    for i in range(t):
        dtnList.append(int(input()))
      
    start = solution(s, graph)
    end1 = solution(g, graph)
    end2 = solution(h, graph)
    rst=[]
    
    for i in range(t):
        x=dtnList[i]
        if start[g]+end1[h]+end2[x] == start[x] or start[h]+end2[g]+end1[x] == start[x]:
            rst.append(x)
    rst.sort()
    print(*rst)