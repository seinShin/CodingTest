import sys
#플로이드 워셜
input = sys.stdin.readline

v,e = map(int, input().split())
INF = int(1e9)
graph = [[INF] *(v+1) for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a][b] = c
    
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[a][b] = min(graph[a][b] , graph[a][k]+graph[k][b])
            
            
rst = INF
for i in range(1,v+1):
    rst = min(rst, graph[i][i])
    
if rst ==INF:
    print(-1)
else:
    print(rst)
    