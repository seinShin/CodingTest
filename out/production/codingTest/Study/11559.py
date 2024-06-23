#11559 뿌요뿌요

import sys
from collections import deque

input = sys.stdin.readline

lst = [list(str(input().strip())) for _ in range(12)]

# test
# lst=[['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', 'Y', '.', '.', '.', '.'], ['.', 'Y', 'G', '.', '.', '.'], ['R', 'R', 'Y', 'G', '.', '.'], ['R', 'R', 'Y', 'G', 'G', '.']]


#같은 것 탐색
dxL=[0,0,-1,1]
dyL=[1,-1,0,0]    

def bfs(i,j,k):
    q = deque()
    q.append((i,j,k))
    lst[i][j] = '.'
    chk=[]
    while q:
        i,j,k = q.popleft()
        chk.append((i,j,k))
        
        for a in range(4):
            dx = i+dxL[a]
            dy = j+dyL[a]
           
            if dx < 0 or dx > 11 or dy <0 or dy > 5:
                continue
           
            if lst[dx][dy] == k and lst[dx][dy] != '.' and (dx,dy,k) not in chk:
                lst[dx][dy] = '.'
                q.append((dx,dy,k))
    #개수 체크
    if len(chk)>=4:
        return len(chk)
    else:
        for x,y,k in chk:
            lst[x][y] = k
        return 0
        
    
#떨어트리기                
def drop():
    for i in range(11, -1, -1):
        for j in range(5, -1, -1):
            if lst[i][j] == '.':
                x = i-1
                while x>=0 and lst[x][j] == '.':
                    x -=1
                if x<0:
                    lst[i][j] = '.'
                else:
                    lst[i][j] = lst[x][j]
                    lst[x][j] = '.'

#main
puyo=0

while True:
    rst=0
    for i in range(12):
        for j in range(6):
            if lst[i][j] != '.':
                rst += bfs(i,j,lst[i][j])

    if rst == 0:
        break
    
    puyo+=1
    drop()
    
print(puyo)

                    
                
                    
                    