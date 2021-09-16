N = int(input())

a=list(map(int,input().split()))
maxi=max(a)
sum=0
for i in range(N):
    a[i] = a[i]/maxi*100
    sum+=a[i]
print(sum/N)
