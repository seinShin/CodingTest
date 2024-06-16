def comb(arr, n):
    rst=[]
    if n>len(arr):
        return False
    
    if n == 1:
        for i in arr:
            rst.append([i])
    elif n>1:
        for i in range(len(arr)-n+1):
            for tmp in range(arr[i+1], n-1):
                rst.append([arr[i]]+tmp)
    
    return rst
        

 ## dfs
from collections import deque
 
m = 3
lst=[12,3,4]
 
def dfs(comb, depth):
    if len(comb) == m:
        return comb
    elif depth == len(lst):
        return 
    
    comb.append(lst[depth])
    dfs(comb, depth+1)
    comb.pop()
    dfs(comb, depth+1)
     
dfs(deque(), 0)