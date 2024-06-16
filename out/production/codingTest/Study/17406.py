# 17406- 배열 돌리기4

from copy import deepcopy
from itertools import permutations
import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
board=[list(map(int, input().split())) for _ in range(n)]

rst = 50*100+1

rcs = [list(map(int, input().split())) for _ in range(k)]

for i in permutations(rcs):
    board2 = deepcopy(board)
    
    for r,c,s in i:
        r -=1
        c -=1
        
        for n in range(s, 0, -1):
            end = board2[r-n][c+n]
            board2[r-n][c-n+1:c+n+1] = board2[r-n][c-n:c+n]
            
            for row1 in range(r-n, r+n):
                board2[row1][c-n] = board2[row1+1][c-n]
            
            board2[r+n][c-n:c+n] = board2[r+n][c-n+1:c+n+1]
            
            for row2 in range(r+n, r-n, -1):
                board2[row2][c+n] = board2[row2-1][c+n]
                
            board2[r-n+1][c+n] = end
            
    for li in board2:
        rst = min(rst, sum(li))
            
print(rst)
                
            
            
            
        
        