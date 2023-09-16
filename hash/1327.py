# 1327 소트 게임
from collections import deque
import sys
input = sys.stdin.readline



def bfs(lst):
    q = deque()
    s = "".join(lst)
    visited[s] = 1
    q.append(lst)
    
    sorting = sorted(lst)
    
    cnt = -1
    
    while q:
        cnt+=1
        print(q)
        for _ in range(len(q)):
            cur = q.popleft()
            
            if cur == sorting:
                return cnt
            
            for i in range(n-k+1):
                start = cur[:i]
                tmp = cur[i:i+k]
                end = cur[i+k:]
                lst2 = start+tmp[::-1]+end
                
                s2 = "".join(lst2)
                
                if s2 not in visited:    
                    visited[s2] =1 
                    q.append(lst2)
                
                
    return -1


n,k = map(int, input().split())
game=list(map(str, input().split()))
visited={}

print(bfs(game))


