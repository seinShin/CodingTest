n, m = map(int, input().split())
lst = [i for i in range(1, n+1)]
    
for i in range(m):
    i,j = map(int, input().split())
    bf = lst[i-1]
    lst[i-1] = lst[j-1]
    lst[j-1] = bf

for i in lst:
    print(i, end=" ")