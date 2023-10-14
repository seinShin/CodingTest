## 재귀
def perm(arr, n):
    rst=[]
    
    if n>len(arr): return False

    if n==1:
        for i in arr:
            rst.append([i])
    elif n>1:
        for i in range(len(arr)):
            ele=arr[i]
            tmp = perm(arr[:i]+arr[i+1:], n-1)
            for p in tmp:
                rst.append([ele]+p)
                
                

 ## dfs
from collections import deque

m=3
lst=[1,2,3,4]
visited=[False] * len(lst)
rst=[]

def dfs(perm):
    if len(perm) == m:
        rst.append(list(perm))
        return rst
    for i, val in enumerate(lst):
        if visited[i]:
            continue
        perm.append(val)
        visited[i] = True
        dfs(perm)
        
        perm.pop()
        visited[i]=False
        
dfs(deque())
        
        
        
 