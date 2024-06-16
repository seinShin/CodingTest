import sys
input = sys.stdin.readline

n,m = map(int, input().split())

parent=[i for i in range(n)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(m):
    a,b = map(int, input().split())
    if find(a) == find(b):
        print(i+1)
        break
    union(a,b)
else:
    print(0)

        

    
