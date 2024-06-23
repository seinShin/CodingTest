a=[]
for i in range(int(input())):
    a.append(int(input()))

for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1],a[j]
for i in a:
    print(i)

            
#sorted() 사용 