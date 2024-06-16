def priTest(n):
    i=1
    rst=0
    while i*i<n:
        if n%i ==0:
            rst +=2
        i+=1
    if i*i == n:
        rst +=1
    return rst

m = int(input())
n = int(input())
con = 0
total = 0
alist = []

for i in range(m,n+1):
    if priTest(i) == 2:
        total += i
        alist.append(i)
        con += 1
if(con == 0):
    print(-1)
else:
    print(total)
    print(alist[0])
    