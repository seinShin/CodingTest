# 6497 전력난
import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
         
while True:
    m,n = map(int, input().split())
    
    if m == n== 0:
        break
    parent=[i for i in range(n+1)]
    edges=[]
    
    for _ in range(n):
        x,y,z = map(int, input().split())
        edges.append([z,x,y])
        
    edges.sort()
    total=0
    for cost,x,y in edges:
        if find(x) != find(y):
            union(x,y)
        else:
            total+= cost
       
    print(total)
    