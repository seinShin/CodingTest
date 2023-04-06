from collections import deque
n = int(input())


for i in range(n):
    n,m = map(int, input().split())
    
    q = list(map(int, input().split()))
    idx = list(range(len(q)))
    idx[m] = 'pv'
    
    order =0
    
    while True:
        if q[0] == max(q):
            order+=1
            
            if idx[0] == 'pv':
                print(order)
                break 
            else:
                q.pop(0)
                idx.pop(0)
        
        else:
            q.append(q.pop(0))
            idx.append(idx.pop(0))                   
                                
        
    
    
    
    
        