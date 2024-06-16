T = int(input())
a=list()
b=list()
c=list()

for i in range(0,T,1):
    A,B = map(int,input().split())
    a.append(A+B)
    b.append(A)
    c.append(B)

for i in range(0,len(a),1):
    print("Case #%d: %d + %d = %d" %(i+1,b[i],c[i],a[i]))

    