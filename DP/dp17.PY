import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp=[0]*n
lst=[]
for _ in range(n):
    w,v = map(int, input().split())
    lst.append([w,v])
    

for i in range(n):
    sum=0
    for j in range(i,n):
        sum += lst[j][0]
        if sum <= k:
            dp[i] += lst[j][1]            
        else:
            sum -= lst[j][0]

print(max(dp))