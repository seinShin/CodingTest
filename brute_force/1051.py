# 1051 숫자 정사각형
import sys
input = sys.stdin.readline

# 정사각형 판별 함수
def chk(i,j):
    x = rac[i][j]
    tmp=1
    for idx in range(1, min(n,m)):
        if i+idx >= n or j+idx >= m:
            continue
        
        y = rac[i][j+idx]
        x2 = rac[i+idx][j]
        y2 = rac[i+idx][j+idx]
        
        if x == y == x2 == y2:
            tmp = max((idx+1)**2, tmp)
    
    return tmp
        
# main 함수
n, m = map(int, input().split())

rac = list()
for i in range(n):
    rac.append(list(input()))
    
size=1
for i in range(n-1):
    for j in range(m-1):    
        size= max(size, chk(i, j))
            
print(size)
            
                
            
