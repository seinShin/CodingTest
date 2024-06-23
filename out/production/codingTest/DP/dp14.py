import sys
input = sys.stdin.readline

n = int(input())

lst=sorted([list(map(int, input().split())) for _ in range(n)])

dp=[1]*(n)
    
for i in range(n):
    for j in range(i):
        if lst[i][1]>lst[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(n-max(dp))