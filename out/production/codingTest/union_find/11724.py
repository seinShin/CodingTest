# 11724 연결 요소의 개수
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
parent =[ i for i in range(n+1)]

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
        
cnt=0
for i in range(m):
    x,y = map(int, input().split())
    union(x,y)

cnt=set()
for i in range(1,n+1):
    cnt.add(find(i))
    
print(len(cnt))