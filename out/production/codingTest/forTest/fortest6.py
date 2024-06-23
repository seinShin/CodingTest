T = int(input())
a =list()

for i in range(0,T,1):
    A,B = map(int,input().split())
    a.append(A+B)
b=0
for i in a:
    b +=1
    print("Case #%d: %d" %(b,i))

    