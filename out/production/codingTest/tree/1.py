import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

graph=[[] for _ in range(n+1)]
parents=[0]*(n+1)

for _ in range(n-1):
    v,x = map(int, input().split())
    graph[v].append(x)
    graph[x].append(v)
    

def dfs(x):
    for i in graph[x]:
        if parents[i] == 0:
            parents[i] = x
            dfs(i)


dfs(1)
for i in range(2, len(parents)):
    print(parents[i])            
        
            
         
