n,k = map(int, input().split())

a,b = [],[]

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    b.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(k):
        print(a[i][j] + b[i][j], end=' ')
    print()

