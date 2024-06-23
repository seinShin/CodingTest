# 4803 트리 - union find 사용

import sys 
input= sys.stdin.readline
flag = True

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x] 

def union(v,u):
    root1=find(v)
    root2=find(u)
    
    if root1<root2:
        parent[root2] = root1
    elif root1>root2:
        parent[root1] = root2
    else:
        for i in range(len(parent)):
            if parent[i] == root1==root2:
                parent[i]=0
cnt = 0
while True:
    cnt+=1
    n,m = map(int, input().split())
    
    if n==0==m:
        break
    
    parent=[0] *(n+1)
    
    for i in range(n+1):
        parent[i]=i
    
    for i in range(m):
        a, b = map(int, input().split())
        union(a,b)
        
    rst=set()
    for i in range(1, n+1):
        if find(i) != 0:
            rst.add(find(i))
        
    size = len(list(rst))
    
    if size == 0:
        print("Case %d: No trees." % cnt)
    elif size == 1:
        print("Case %d: There is one tree." % cnt)
    else:
        print("Case %d: A forest of %d trees." % (cnt ,size))
        
    