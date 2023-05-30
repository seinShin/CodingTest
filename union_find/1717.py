import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n,m = map(int, input().split())

graph=[i for i in range(n+1)]

def find(x):
    if graph[x] != x:
        graph[x] = find(graph[x])
    return graph[x]


def union(a,b):
    a = find(a)
    b = find(b)
    
    if a < b: 
        graph[b] = a
    else:
        graph[a] = b
        
for _ in range(m):
    state, a, b = map(int, input().split())
    
    if state == 0:
        union(a,b)     
    elif state == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
            


    