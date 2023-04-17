import sys
input = sys.stdin.readline
n = int(input())

lst = [list(map(int, input().split())) for i in range(n)]

rst=[]
def dc(x,y,n):
    pv = lst[x][y]
    
    for i in range(x,x+n):
        for j in range(y,y+n):
            if pv != lst[i][j]:
                dc(x,y,n//3)
                dc(x,y+n//3,n//3)
                dc(x,y+n//3*2,n//3)
                dc(x+n//3,y,n//3)
                dc(x+n//3,y+n//3,n//3)
                dc(x+n//3,y+n//3*2,n//3)
                dc(x+n//3*2,y,n//3)
                dc(x+n//3*2,y+n//3,n//3)
                dc(x+n//3*2,y+n//3*2,n//3)
                return
    if pv == 0:
        rst.append(0)
    elif pv == -1:
        rst.append(-1)
    else:
        rst.append(1)

dc(0,0,n)
print(rst.count(-1))
print(rst.count(0))
print(rst.count(1))