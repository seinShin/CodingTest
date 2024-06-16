import sys
n = int(sys.stdin.readline())
lst=[]
for _ in range(n):
    lst.append(list(map(int, input().split())))
    
for i in range(1, n):
    for j in range(0,i+1):
        if j == 0:    
            lst[i][0] = lst[i-1][0] + lst[i][0]
        elif j !=0 and j == i:
            lst[i][j] = lst[i-1][j-1] + lst[i][j]
        else:
            lst[i][j] = max(lst[i-1][j] ,lst[i-1][j-1]) + lst[i][j]
print(max(lst[n-1]))    