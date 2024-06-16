n, m = map(int, input().split())
lst = [0 for i in range(n)]

for i in range(m):
    i,j,k = map(int, input().split())
    for i in range(i,j+1):
        lst[i-1] = k

for i in lst:
    print(i, end=" ")