import sys
input = sys.stdin.readline

n = int(input())

lst=[list(map(int, input().split())) for _ in range(n)]

rst=[]

def dc(x,y,n):
    color = lst[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != lst[i][j]:
                dc(x, y , n//2)
                dc(x, y+n//2, n//2)
                dc(x+n//2, y, n//2)
                dc(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        rst.append(0)
    else:
        rst.append(1)
        
dc(0,0,n)
print(rst.count(0))
print(rst.count(1))

