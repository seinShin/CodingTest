T = int(input())
arr=[]
for i in range(0,T,1):
    A, B = map(int,input().split())
    sum = A + B
    arr.append(sum) 
for i in arr:
    print(i)
