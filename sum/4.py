import sys
input = sys.stdin.readline
n,m = map(int, input().split())

tmp = [[0]*n for _ in range(n)]
lst=[]

for i in range(n):
    lst.append(list(map(int, input().split())))
    

for i in range(n):
    sum = 0
    for j in range(n):
        sum += lst[i][j]
        tmp[i][j] = sum

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    
    start = y1-2
    
    if x1==x2 and y1==y2:
        print(lst[x1-1][y1-1])
    else:
        sum=0
        for i in range(x1-1, x2 ):
            if start<0:
                sum += tmp[i][y2-1]
            else:
                sum += tmp[i][y2-1]-tmp[i][y1-2]
        print(sum)    
                
         
    
    
    
# for i in range(n):
#     for j in range(n):
#         sum += lst[i][j]
#         tmp[i][j] = sum
        
# for i in range(m):
#     x1, y1, x2, y2 = map(int, input().split())
#     if x1 == x2 and y1 == y2:
#         print(lst[x1-1][y2-1])
#     elif x1 == y1 == 1 and x2==y2==n:
#         print(tmp[x2-1][y2-1])
#     else:
#         print(tmp[x2-1][y2-1] - tmp[x1-1][y1-1])