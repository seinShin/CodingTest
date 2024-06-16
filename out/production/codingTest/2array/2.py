a =[]
b=[]

for i in range(9):
    a.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        b.append(a[i][j])


for i in range(9):
    for j in range(9):
        if a[i][j] == max(b):
            print(max(b), sep='')
            print(i+1 ," ", j+1)

    